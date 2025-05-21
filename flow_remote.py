from prefect import flow, task, get_run_logger

@flow
def hello_remote():
    logger = get_run_logger()
    logger.info("Inizio hello_remote change on fly!")
    for i in [1,2,3,4]:
        logger.info(f"loop hello_remote item:{i}")
    logger.info("hello_remote completato con successo.")
    
if __name__ == "__main__":
    hello_remote()
    