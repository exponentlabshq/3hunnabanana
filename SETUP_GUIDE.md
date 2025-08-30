# 🚀 Complete Setup Guide - 3HunnaBanana AI Content Generator

## ✨ What You'll Get

**3HunnaBanana** now generates **THREE types of content** from a single prompt:

1. **📝 Rich Text Descriptions** (Always works)
2. **🖼️ AI-Generated Images** (Optional setup)
3. **🎬 AI-Generated Videos** (Automatic with Gemini API)

## 🎯 Quick Start (3 Steps)

### Step 1: Get Your Free API Keys

#### A. Gemini API (Required!)
- 🌐 **URL**: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
- 📝 **Steps**:
  1. Create free Google account
  2. Visit Google AI Studio
  3. Click "Get API key"
  4. Copy the generated key

#### B. Hugging Face API (For Images)
- 🌐 **URL**: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- 📝 **Steps**:
  1. Create free account
  2. Click "New token"
  3. Name it "3HunnaBanana"
  4. Select "Read" role
  5. Copy token (starts with "hf_")

### Step 2: Update Configuration

Open `config.py` and update:

```python
# Gemini API Key (Required!)
GEMINI_API_KEY = "your_actual_gemini_api_key_here"  # ← Update this!

# Hugging Face API Key (Optional - for images)
HUGGINGFACE_API_KEY = "hf_your_actual_token_here"  # ← Update this!
```

### Step 3: Restart & Test

```bash
python3 app.py
```

Visit: `http://localhost:5000`

## 🎨 Content Generation Examples

### Text Prompts That Work Great:

**Images & Videos:**
- "A magical forest with glowing mushrooms at twilight"
- "A cyberpunk city street with neon lights and rain"
- "A steampunk airship flying over Victorian London"
- "A serene Japanese garden with cherry blossoms falling"

**Creative Scenes:**
- "A wizard casting spells in an ancient library"
- "A robot playing chess with a human in a futuristic cafe"
- "A dragon sleeping on a pile of golden treasure"

## 🔧 Advanced Configuration

### Image Quality Settings

```python
# In config.py
INFERENCE_STEPS = 30      # Higher = better quality (slower)
GUIDANCE_SCALE = 8.5      # Higher = more prompt adherence
IMAGE_WIDTH = 768         # Larger images (if model supports)
IMAGE_HEIGHT = 768
```

### Video Generation Settings

The Veo API automatically uses optimal settings:
- **Model**: Veo 3.0 (latest)
- **Quality**: High definition
- **Duration**: Automatic based on prompt
- **Style**: Cinematic and professional

## 🚨 Troubleshooting

### Common Issues & Solutions

#### No Images Generated?
- ✅ Check `HUGGINGFACE_API_KEY` in `config.py`
- ✅ Verify your Hugging Face account is verified
- ✅ First request might take 1-2 minutes (model loading)

#### No Videos Generated?
- ✅ Gemini API key should work automatically
- ✅ Check console for Veo API errors
- ✅ Video generation takes 5-10 minutes

#### API Rate Limits?
- **Gemini**: Generous free tier
- **Hugging Face**: Free tier available
- **Veo**: Uses Gemini quota

### Error Messages

```
"Hugging Face API key not configured"
→ Update HUGGINGFACE_API_KEY in config.py

"Veo API error: 403"
→ Check Gemini API key validity

"Address already in use"
→ Kill existing process: pkill -f "python3 app.py"
```

## 📱 Using the Web Interface

1. **Enter Prompt**: Type your creative description
2. **Click Generate**: AI processes your request
3. **View Results**: 
   - Text description appears immediately
   - Image loads (if configured)
   - Video status shows progress
4. **Download**: Right-click images to save

## 🎯 Pro Tips

- **Be Specific**: "A red dragon breathing fire" vs "a dragon"
- **Include Style**: "in the style of Studio Ghibli" or "cyberpunk aesthetic"
- **Add Details**: "with dramatic lighting" or "at sunset"
- **Combine Elements**: "A steampunk robot in a Victorian garden"

## 🔗 Useful Links

- **Google AI Studio**: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
- **Hugging Face**: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- **Project Repository**: Your local 3HunnaBanana folder

## 🎉 You're Ready!

With this setup, you'll have:
- ✅ **Text**: Rich, artistic descriptions
- ✅ **Images**: 512x512 AI-generated artwork  
- ✅ **Videos**: Cinematic AI-generated videos
- ✅ **All Free**: No costs, no limits for personal use

**Happy creating!** 🎨✨🎬
