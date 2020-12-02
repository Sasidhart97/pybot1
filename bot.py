# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
#import torch
from model1 import models
#from sentence_transformers import SentenceTransformer, util
#saved_model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
pid=["Hello and Welcome"]
class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    #global saved_model
    global pid
    async def on_message_activity(self, turn_context: TurnContext):
        pid.append(str(turn_context.activity.text))
        await turn_context.send_activity(models(turn_context.activity.text,pid[-2]))
        
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                #print("\nMember added: ",member_added.id)
                #pid=str(member_added.id)
                await turn_context.send_activity("Hello and welcome!")
