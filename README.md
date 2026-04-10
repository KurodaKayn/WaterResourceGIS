# Water Resource GIS

基于 `methodology.docx` 指导手册构建的水利信息系统项目骨架。

## 已实现内容（第一阶段）

- 严格按手册创建目录结构（docs/data/src/tests/config/scripts/deployment）
- FastAPI 应用入口与基础路由：
  - `GET /health`
  - `GET /api/v1/water-features`
  - `POST /api/v1/analysis/buffer`
- 分层代码结构：`core -> modules -> repositories -> services -> api`
- 基础空间数据模型（PostGIS）：
  - `water_features`
  - `monitoring_stations`
- 基础校验、异常处理与统一错误格式
- Docker + docker-compose 部署基础文件
- pytest 基础测试样例

## 快速开始

1. 创建虚拟环境并安装依赖

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. 配置环境变量

```bash
cp .env.example .env
```

3. 启动依赖服务（PostGIS + Redis）

```bash
docker compose -f deployment/docker/docker-compose.yml up -d database redis
```

4. 初始化数据库

```bash
python scripts/setup_database.py
```

5. 启动服务

```bash
uvicorn src.main:app --reload
```

6. 运行测试

```bash
pytest
```

## 后续开发计划（第二阶段）

- 完整实现 CRUD（water-features / stations）
- 增加 Alembic 迁移与分区表（monitoring_readings）
- 完成 RBAC、JWT、审计日志
- 实现空间叠加分析、拓扑检查和网络分析
- 增补 OpenAPI 文档和数据导入流水线
