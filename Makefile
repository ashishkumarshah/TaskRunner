SERVICE_NAME = taskrunner
IMAGE_NAME = taskrunner:latest
CONTAINER_NAME = taskrunner

DB_FILE = db/itemstatus.db
SQL_FILE = itemstatus.sql

.DEFAULT_GOAL := install

.PHONY: install uninstall clean status logs installdb

installdb: $(DB_FILE)

$(DB_FILE): $(SQL_FILE)
	sqlite3 $(DB_FILE) < $(SQL_FILE)

clean:
	rm -f $(DB_FILE)

install: installdb
	pip3 install --no-cache-dir -r requirements.txt
	mkdir -p /TaskRunner
	cp -r . /TaskRunner/
	sudo cp service/etc/systemd/system/$(SERVICE_NAME).service /etc/systemd/system/
	sudo cp service/etc/systemd/system/$(SERVICE_NAME).timer /etc/systemd/system/
	sudo systemctl daemon-reload
	sudo systemctl enable --now $(SERVICE_NAME).timer

uninstall:
	sudo systemctl disable --now $(SERVICE_NAME).timer || true
	sudo rm -f /etc/systemd/system/$(SERVICE_NAME).service
	sudo rm -f /etc/systemd/system/$(SERVICE_NAME).timer
	sudo systemctl daemon-reload

status:
	systemctl status $(SERVICE_NAME).timer
	systemctl status $(SERVICE_NAME).service

logs:
	journalctl -u $(SERVICE_NAME).service -f
