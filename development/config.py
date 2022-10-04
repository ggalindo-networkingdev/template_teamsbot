#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "d0713242-3a8b-4387-b6cb-f3f7e02df6cc")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "9LM8Q~hrxvFA1E5ABtBXWFtvHar~dfPgE-IgtbL~")
