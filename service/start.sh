#!/bin/bash
set -e

# Reload systemd units & enable timer
systemctl daemon-reload
systemctl enable --now taskrunner.timer

# Hand off to systemd as PID 1
exec /sbin/init
