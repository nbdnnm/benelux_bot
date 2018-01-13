#!/usr/bin/env bash
kill $(ps aux | grep '[p]ython benelux_bot.py' | awk '{print $2}')
