# Speaker Diarization Web Application

A full-stack web application that automatically separates audio files by different speakers using AI-powered speaker diarization.

## Features

- 🎵 **Audio Upload**: Support for WAV, MP3, M4A, FLAC, and AAC files
- 🧠 **AI-Powered**: Uses pyannote.audio for accurate speaker detection
- 🎯 **Two-Speaker Focus**: Optimized for conversations with exactly 2 speakers
- 📱 **Modern UI**: Clean, responsive interface built with React and TailwindCSS
- ⚡ **Real-time Processing**: Live status updates during processing
- 📥 **Easy Downloads**: Direct download links for separated audio files

## Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **pyannote.audio**: State-of-the-art speaker diarization
- **pydub**: Audio manipulation and processing
- **PyTorch**: Deep learning backend

### Frontend
- **React 18**: Modern React with hooks
- **Vite**: Fast build tool and dev server
- **TailwindCSS**: Utility-first CSS framework
- **Axios**: HTTP client for API communication

## Prerequisites

- Python 3.11+
- Node.js 18+
- Docker (optional, for containerized deployment)
- HuggingFace account (for pyannote.audio model access)

## Quick Start

### Option 1: Docker Compose (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd HeartDiseaseApp
   ```

2. **Set up HuggingFace token**
   - Create a HuggingFace account at https://huggingface.co
   - Accept the license for pyannote/speaker-diarization-3.1
   - Generate an access token
   - Update `backend/audio_processor.py` with your token:
     ```python
     use_auth_token="your_huggingface_token_here"
     ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000

### Option 2: Manual Setup

#### Backend Setup

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up HuggingFace token**
   - Update `backend/audio_processor.py` with your HuggingFace token

4. **Run the backend**
   ```bash
   cd backend
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

#### Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Run the frontend**
   ```bash
   npm run dev
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000

## Usage

1. **Upload Audio**: Drag and drop or click to select an audio file
2. **Processing**: Wait while the system detects and separates speakers
3. **Download**: Get separate audio files for each speaker

## API Endpoints

### Upload Audio
```
POST /upload
Content-Type: multipart/form-data
Body: audio file
Response: { "job_id": "uuid", "status": "uploaded" }
```

### Check Status
```
GET /status/{job_id}
Response: { "status": "completed", "speaker1_download": "/download/speaker1/{job_id}" }
```

### Download Files
```
GET /download/speaker1/{job_id}
GET /download/speaker2/{job_id}
Response: Audio file download
```

### Cleanup
```
DELETE /cleanup/{job_id}
Response: { "message": "Cleanup completed" }
```

## Configuration

### Environment Variables

- `PYTHONPATH`: Set to `/app` for Docker deployment
- `REACT_APP_API_URL`: Backend API URL for frontend

### File Limits

- Maximum file size: 100MB
- Supported formats: WAV, MP3, M4A, FLAC, AAC
- Processing timeout: 5 minutes

## Development

### Project Structure
```
├── backend/
│   ├── main.py              # FastAPI application
│   └── audio_processor.py   # Audio processing logic
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── services/        # API services
│   │   └── App.jsx         # Main application
│   └── package.json
├── docker-compose.yml       # Docker orchestration
├── Dockerfile              # Backend container
└── requirements.txt        # Python dependencies
```

### Adding Features

1. **Backend**: Add new endpoints in `backend/main.py`
2. **Frontend**: Create components in `frontend/src/components/`
3. **API**: Update services in `frontend/src/services/api.js`

## Troubleshooting

### Common Issues

1. **HuggingFace Token Error**
   - Ensure you have accepted the model license
   - Verify your token is correctly set in `audio_processor.py`

2. **Audio Processing Fails**
   - Check file format compatibility
   - Ensure audio file is not corrupted
   - Verify sufficient disk space

3. **CORS Errors**
   - Ensure backend is running on port 8000
   - Check CORS configuration in `main.py`

4. **Docker Issues**
   - Ensure Docker and Docker Compose are installed
   - Check if ports 3000 and 8000 are available

### Logs

- Backend logs: Check Docker logs with `docker-compose logs backend`
- Frontend logs: Check browser console for errors

## Performance Notes

- Processing time depends on audio length and complexity
- Typical processing: 1-2 minutes per minute of audio
- Files are automatically cleaned up after 24 hours
- Consider using GPU acceleration for faster processing

## Security Considerations

- Files are stored temporarily and cleaned up automatically
- No persistent storage of uploaded audio files
- CORS is configured for development; update for production
- Consider adding authentication for production use

## License

This project is for educational and development purposes. Please ensure you comply with the pyannote.audio model license terms.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the logs for error messages
3. Ensure all dependencies are correctly installed
4. Verify HuggingFace token configuration
