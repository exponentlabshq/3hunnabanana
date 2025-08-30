async function generateContent() {
    const promptInput = document.getElementById('promptInput');
    const generateBtn = document.getElementById('generateBtn');
    const resultSection = document.getElementById('resultSection');
    const resultContent = document.getElementById('resultContent');
    const loadingSpinner = document.getElementById('loadingSpinner');
    
    const prompt = promptInput.value.trim();
    
    if (!prompt) {
        alert('Please enter a prompt to generate content.');
        return;
    }
    
    // Show loading state
    generateBtn.disabled = true;
    generateBtn.textContent = 'Generating...';
    resultSection.style.display = 'block';
    resultContent.style.display = 'none';
    loadingSpinner.style.display = 'block';
    
    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: prompt })
        });
        
        const data = await response.json();
        
        if (data.success) {
            let contentHTML = `
                <h4>Generated Response:</h4>
                <p>${data.response}</p>
                <p><em>${data.message}</em></p>
            `;
            
            // Add video status if generated
            if (data.has_video && data.video_status) {
                contentHTML += `
                    <div class="generated-video">
                        <h4>🎬 Video Generation:</h4>
                        <p><strong>Status:</strong> ${data.video_status}</p>
                        <p><em>Note: Video generation is in progress. This may take several minutes.</em></p>
                    </div>
                `;
            }
            
            // Add image if generated
            if (data.has_image && data.image_status && data.image_status.startsWith('data:image')) {
                contentHTML += `
                    <div class="generated-image">
                        <h4>🖼️ Generated Image:</h4>
                        <img src="${data.image_status}" alt="AI Generated Image" style="max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
                    </div>
                `;
            } else if (data.has_image && data.image_status) {
                contentHTML += `
                    <div class="generated-image">
                        <h4>🖼️ Image Generation:</h4>
                        <p><strong>Status:</strong> ${data.image_status}</p>
                    </div>
                `;
            }
            
            // Show status if no media generated
            if (!data.has_image && !data.has_video) {
                contentHTML += `
                    <div class="status-note">
                        <h4>🚀 Google AI Services Status:</h4>
                        <p><strong>✅ Text Generation:</strong> Working (Gemini 2.5 Flash)</p>
                        <p><strong>🎬 Video Generation:</strong> Available (Veo 3.0)</p>
                        <p><strong>🖼️ Image Generation:</strong> Available (Gemini 2.5 Flash Image)</p>
                        <p><em>All services use the same Google API key automatically!</em></p>
                    </div>
                `;
            }
            
            resultContent.innerHTML = contentHTML;
        } else {
            resultContent.innerHTML = `
                <h4>Error:</h4>
                <p>${data.error}</p>
            `;
        }
        
        resultContent.style.display = 'block';
        
    } catch (error) {
        resultContent.innerHTML = `
            <h4>Error:</h4>
            <p>Failed to generate content: ${error.message}</p>
        `;
        resultContent.style.display = 'block';
    } finally {
        // Reset button state
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Content';
        loadingSpinner.style.display = 'none';
    }
}

// Add enter key support for the textarea
document.getElementById('promptInput').addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && e.ctrlKey) {
        generateContent();
    }
});
