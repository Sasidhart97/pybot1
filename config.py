#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "bada8524-e445-4a2d-86f7-815507f729c6")
    
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "3.u3BE.n.07d7s4o8.~fE0~O69E_Cba~bc")
