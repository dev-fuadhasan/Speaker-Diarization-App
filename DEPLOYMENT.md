# Deployment Guide

This guide covers deploying the Speaker Diarization application to production.

## Architecture Overview

- **Frontend**: React app deployed to Netlify
- **Backend**: FastAPI app deployed to Railway/Render/Heroku
- **Storage**: Temporary file storage on backend platform

## Option 1: Netlify + Railway (Recommended)

### Frontend Deployment (Netlify)

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy to Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub repository
   - Build settings:
     - Build command: `cd frontend && npm run build`
     - Publish directory: `frontend/build`
   - Add environment variable:
     - `REACT_APP_API_URL`: Your Railway backend URL

### Backend Deployment (Railway)

1. **Prepare for Railway:**
   ```bash
   # Install Railway CLI
   npm install -g @railway/cli
   
   # Login to Railway
   railway login
   ```

2. **Deploy Backend:**
   ```bash
   # Initialize Railway project
   railway init
   
   # Set environment variables
   railway variables set HUGGINGFACE_TOKEN=your_token_here
   
   # Deploy
   railway up
   ```

3. **Get Backend URL:**
   - Railway will provide a URL like: `https://your-app.railway.app`
   - Update Netlify environment variable with this URL

## Option 2: Netlify + Render

### Backend Deployment (Render)

1. **Connect GitHub to Render:**
   - Go to [render.com](https://render.com)
   - Connect your GitHub account
   - Create new "Web Service"

2. **Configure Render Service:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables:
     - `HUGGINGFACE_TOKEN`: Your HuggingFace token
     - `PYTHONPATH`: `/opt/render/project/src`

3. **Update Frontend:**
   - Set `REACT_APP_API_URL` in Netlify to your Render URL

## Option 3: Full Docker Deployment

### Using Railway with Docker

1. **Update docker-compose.yml for production:**
   ```yaml
   version: '3.8'
   services:
     backend:
       build: .
       ports:
         - "8000:8000"
       environment:
         - HUGGINGFACE_TOKEN=${HUGGINGFACE_TOKEN}
       restart: unless-stopped
   ```

2. **Deploy with Railway:**
   ```bash
   railway up --dockerfile Dockerfile
   ```

## Environment Variables

### Frontend (Netlify)
- `REACT_APP_API_URL`: Backend API URL

### Backend (Railway/Render/Heroku)
- `HUGGINGFACE_TOKEN`: Your HuggingFace access token
- `PYTHONPATH`: `/opt/render/project/src` (for Render)

## Important Considerations

### File Storage
- Backend platforms have limited temporary storage
- Files are automatically cleaned up after processing
- Consider using cloud storage (AWS S3, Google Cloud) for production

### Performance
- AI model loading takes time on first request
- Consider keeping the model warm with health checks
- Monitor memory usage (models are large)

### Security
- Never commit tokens to Git
- Use environment variables for all secrets
- Enable CORS only for your frontend domain

## Monitoring

### Health Checks
- Backend: `GET /` endpoint
- Frontend: Built-in Netlify monitoring

### Logs
- Railway: `railway logs`
- Render: Dashboard logs section
- Netlify: Build logs in dashboard

## Troubleshooting

### Common Issues

1. **CORS Errors:**
   - Update CORS origins in `backend/main.py`
   - Add your Netlify domain to allowed origins

2. **Model Loading Failures:**
   - Verify HuggingFace token is correct
   - Check if model license is accepted
   - Ensure sufficient memory allocation

3. **File Upload Issues:**
   - Check file size limits
   - Verify temporary directory permissions
   - Monitor disk space usage

### Performance Optimization

1. **Model Caching:**
   - Models are cached after first load
   - Consider using model quantization for faster loading

2. **File Processing:**
   - Implement file size limits
   - Add progress indicators
   - Use background job processing

## Cost Considerations

### Free Tiers
- **Netlify**: 100GB bandwidth, 300 build minutes
- **Railway**: $5 credit monthly
- **Render**: 750 hours free tier

### Scaling
- Monitor usage and upgrade plans as needed
- Consider serverless functions for cost optimization
- Implement request rate limiting

## Production Checklist

- [ ] Environment variables configured
- [ ] CORS settings updated for production domain
- [ ] File size limits implemented
- [ ] Error handling and logging configured
- [ ] Health checks working
- [ ] SSL certificates enabled
- [ ] Monitoring and alerts set up
- [ ] Backup strategy for temporary files
- [ ] Performance testing completed
