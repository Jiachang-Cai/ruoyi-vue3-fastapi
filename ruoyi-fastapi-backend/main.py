import uvicorn
from server import app, AppConfig

if __name__ == '__main__':
    uvicorn.run(
        app='main:app', # 模块路径:应用对象名
        host=AppConfig.app_host,
        port=AppConfig.app_port,
        # root_path=AppConfig.app_root_path,
        reload=AppConfig.app_reload,
    )
