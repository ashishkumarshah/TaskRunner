SERVICE_NAME = taskrunner
IMAGE_NAME = taskrunner:latest
CONTAINER_NAME = taskrunner

install:
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

