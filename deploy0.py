from prefect.deployments import Deployment

from flow0 import flow0

Deployment.build_from_flow(
    flow=flow0,
    name="Hello Local",
    work_pool_name="sss2"
).deploy()