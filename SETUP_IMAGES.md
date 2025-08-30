# 🖼️ Image Generation Setup Guide

## Quick Start (3 Steps)

### 1. Get Free Hugging Face Token
- Go to: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- Create a free account (if you don't have one)
- Click "New token"
- Give it a name like "3HunnaBanana"
- Select "Read" role
- Copy the token (starts with "hf_")

### 2. Update Your Config
Open `config.py` and change this line:
```python
HUGGINGFACE_API_KEY = "hf_xxx"  # Replace with your actual token
```

To:
```python
HUGGINGFACE_API_KEY = "hf_your_actual_token_here"
```

### 3. Restart the App
```bash
python3 app.py
```

## What You'll Get

✅ **Text Descriptions**: Always work (Gemini AI)  
✅ **Actual Images**: 512x512 pixel images generated from your prompts  
✅ **Free Service**: No cost, no limits for personal use  

## Test It

1. Go to `http://localhost:5000`
2. Type: "a magical forest with glowing mushrooms"
3. Click "Generate Image"
4. You'll see both the description AND the generated image!

## Troubleshooting

- **No images showing?** Check your API key in `config.py`
- **API errors?** Make sure your Hugging Face account is verified
- **Slow generation?** First request might take 1-2 minutes (model loading)

## Advanced Settings

You can adjust image quality in `config.py`:
```python
IMAGE_WIDTH = 512      # Image width
IMAGE_HEIGHT = 512     # Image height  
INFERENCE_STEPS = 20   # Higher = better quality (slower)
GUIDANCE_SCALE = 7.5   # Higher = more prompt adherence
```

That's it! Enjoy generating AI images! 🎨✨
