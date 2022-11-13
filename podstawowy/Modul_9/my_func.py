def wait_for_time(to_wait: float) -> None:
    from time import sleep
    print(f"Waiting for {to_wait} seconds")
    sleep(to_wait)
    print("Waiting done")
