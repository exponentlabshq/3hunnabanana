import os
import base64
import io
import requests
import time
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from PIL import Image
from config import Config

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = Config.GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    try:
        prompt = request.json.get('prompt')
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        # Use Gemini 2.5 Flash for text generation
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Create a detailed prompt for content generation
        enhanced_prompt = f"""Create a detailed description of content based on this prompt: "{prompt}"

Please provide:
1. Visual composition and layout
2. Color palette and lighting
3. Style and artistic approach
4. Specific details and elements
5. Mood and atmosphere

Make it vivid and detailed enough that an artist could create it."""
        
        # Generate content based on prompt
        response = model.generate_content(enhanced_prompt)
        
        # Try to generate video using Google's Veo API
        video_status = None
        try:
            video_status = generate_video_with_veo(prompt)
        except Exception as vid_error:
            print(f"Video generation failed: {vid_error}")
        
        # Try to generate image using Google's Gemini image generation
        image_status = None
        try:
            image_status = generate_image_with_gemini(prompt)
        except Exception as img_error:
            print(f"Image generation failed: {img_error}")
        
        return jsonify({
            'success': True,
            'response': response.text,
            'message': 'Content generated successfully using Google AI services',
            'video_status': video_status,
            'has_video': video_status is not None,
            'image_status': image_status,
            'has_image': image_status is not None
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_video_with_veo(prompt):
    """
    Generate video using Google's Veo 3.0 API.
    """
    try:
        base_url = "https://generativelanguage.googleapis.com/v1beta"
        api_url = f"{base_url}/models/veo-3.0-generate-preview:predictLongRunning"
        
        headers = {
            "x-goog-api-key": GEMINI_API_KEY,
            "Content-Type": "application/json"
        }
        
        payload = {
            "instances": [{
                "prompt": prompt
            }]
        }
        
        print(f"Generating video for prompt: {prompt}")
        
        # Start the video generation
        response = requests.post(api_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            operation_name = data.get('name')
            
            if operation_name:
                print(f"Video generation started: {operation_name}")
                return f"Video generation in progress: {operation_name}"
            else:
                print("No operation name received")
                return None
        else:
            print(f"Veo API error: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        print(f"Veo API error: {e}")
        return None

def generate_image_with_gemini(prompt):
    """
    Generate image using Google's Gemini image generation.
    """
    try:
        # Use Gemini 2.5 Flash with image generation capability
        model = genai.GenerativeModel('gemini-2.5-flash-image-preview')
        
        print(f"Generating image for prompt: {prompt}")
        
        # Generate image
        response = model.generate_content(prompt)
        
        if response and hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                for part in candidate.content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        # Convert image data to base64 for display
                        image_data = part.inline_data.data
                        image_base64 = base64.b64encode(image_data).decode('utf-8')
                        return f"data:image/png;base64,{image_base64}"
        
        print("No image data in response")
        return None
            
    except Exception as e:
        print(f"Gemini image generation error: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
