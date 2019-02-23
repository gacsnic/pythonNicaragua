#!/bin/bash
watch -d '/usr/sbin/rabbitmqctl list_queues -p python_ni_app name messages messages_ready messages_unacknowledged consumers| sort'
