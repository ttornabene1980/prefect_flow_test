prefect config view

export PREFECT_API_DATABASE_CONNECTION_URL=postgresql+asyncpg://usr_sitre:usr_sitre@10.198.168.98:5432/sorgente

export PREFECT_API_DATABASE_CONNECTION_URL=postgresql+asyncpg://prefect:prefect@10.198.168.98:5432/sorgente

export PREFECT_API_DATABASE_CONNECTION_URL=sqlite+aiosqlite:////Users/tindarotornabene/.prefect/prefect.db

prefect config set PREFECT_API_DATABASE_CONNECTION_URL=sqlite+aiosqlite:////Users/tindarotornabene/.prefect/prefect.db
 
export PREFECT_API_URL='http://0.0.0.0:4200/api'
prefect config set PREFECT_API_URL=http://0.0.0.0:4200/api


export PREFECT_API_URL='https://prefect-server-aria-enttbl-sorgente.apps.rocp-pi-app01.c2ra.p1.openshiftapps.com/api'

prefect config set PREFECT_API_URL='https://prefect-server-aria-enttbl-sorgente.apps.rocp-pi-app01.c2ra.p1.openshiftapps.com/api'

🚀 you are connected to:
http://0.0.0.0:4200
PREFECT_PROFILE='local'
PREFECT_API_URL='http://0.0.0.0:4200/api' (from profile)


prefect server start --host 0.0.0.0

prefect worker start --pool tino




prefect worker start --pool 10_199_147_12



View Deployment in UI: http://0.0.0.0:4200/deployments/deployment/68fb0463-9757-48fa-a23a-ccb75f5a684b



Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/your_custom_key
  IdentitiesOnly yes


  
? Would you like to save configuration for this deployment for faster deployments in the future? [y/n]: y

Deployment configuration saved to prefect.yaml! You can now deploy using this deployment configuration with:

        $ prefect deploy -n default

You can also make changes to this deployment configuration by making changes to the YAML file.

To execute flow runs from these deployments, start a worker in a separate terminal that pulls work from the 
None work pool:

        $ prefect worker start --pool None

To schedule a run for this deployment, use the following command:

        $ prefect deployment run 'hello/default'


prefect deploy -n hello_remote


To execute flow runs from these deployments, start a worker in a separate terminal that pulls work from the 
None work pool:

        $ prefect worker start --pool None

To schedule a run for this deployment, use the following command:
passa parameter
prefect deployment run 'SFTP Get All Files/flow1' \
  --param host="10.199.146.28" \
  --param username="sebc" \
  --param password="sebc" \
  --param remote_directory="/home/sebc/sorgente_mefa_memdif/tino" \
  --param local_directory="/Users/tindarotornabene/develop/sorgente/mia-pipeline/prefect-flow1/data_share" 
