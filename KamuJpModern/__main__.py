from KamuJpModern import KamuJpModern

if __name__ == "__main__":
    import time

    logger = KamuJpModern().modernLogging("main")
    logger.log("This is a test message", "INFO")
    logger.log("This is a warning message", "WARNING")
    logger.log("This is an error message", "ERROR")
    logger.log("This is a debug message", "DEBUG")

    progress_bar1 = KamuJpModern().modernProgressBar(100, "Task 1", 32)
    progress_bar1.setMessage("WAITING")
    progress_bar2 = KamuJpModern().modernProgressBar(200, "Task 2", 34)
    progress_bar2.setMessage("WAITING")

    progress_bar1.start()
    progress_bar2.start()

    progress_bar1.notbusy()
    progress_bar1.setMessage("RUNNING")
    for i in range(100):
        time.sleep(0.05)
        progress_bar1.update()
    progress_bar1.setMessage("DONE")
    progress_bar1.finish()

    progress_bar2.setMessage("RUNNING (BACKGROUND)")
    for i in range(100):
        time.sleep(0.05)
        progress_bar2.update(2)
    progress_bar2.setMessage("DONE")
    progress_bar2.finish()
