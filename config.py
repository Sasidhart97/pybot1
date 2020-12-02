#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "2ee61ad0-7906-4374-a42c-37d1b36ec3c9")
    
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "3.u3BE.n.07d7s4o8.~fE0~O69E_Cba~bc")
