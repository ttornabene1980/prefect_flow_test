from prefect import flow, task, get_run_logger


@flow
def hello():
    logger = get_run_logger()
    logger.info("Inizio flow0!")
    for i in [1,2]:
        logger.info(f"loop flow0 item:{i}")
    logger.info("flow0 completato con successo.")
    
    
if __name__ == "__main__":
    hello()
    