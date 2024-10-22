from typing import Dict, Any

config: Dict[str, Any] = {
    "app": "FastAPI_Rest:app",
    "host": "0.0.0.0",
    "port": 8000,
    "reload": True,
    "workers": 1,
    "log_level": "info",
}
