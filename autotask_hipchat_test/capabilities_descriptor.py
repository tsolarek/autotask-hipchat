capabilities = {
                "name": "Autotask for Hipchat",
                "description": "An integration that provides notifications and limited control functions for the Autotask time tracking software",
                "key": "hipchat-autotask-add-on",
                "links": {
                    "homepage": "https://c669256a.ngrok.io/hipchat-autotask",
                    "self": "https://c669256a.ngrok.io/hipchat-autotask/capabilities"
                },
                "capabilities": {
                    "hipchatApiConsumer": {
                        "scopes": [
                            "send_notification",
                            "view_messages",
                            "view_group",
                            "view_room"
                        ],
                        "fromName": "Autotask"
                    },
                    "installable": {
                        "callbackUrl": "https://c669256a.ngrok.io/hipchat-autotask/installable",
                        "unistalledUrl": "https://c669256a.ngrok.io/hipchat-autotask/uninstalled"
                    },
                    "action": [
                        {
                            "key": "myaddon-action-opendialog",
                            "name":{
                                "value": "Open dialog"
                            },
                            "target": "test-dialog", "location": "hipchat.input.action"
                        }
                    ],
                    "webhook": [
                        {
                            "url": "https://c669256a.ngrok.io/hipchat-autotask/6e4bc5e465456a4fae109743b3c270e2c297ae6b43ce6df64a",
                            "event": "room_message",
                            "name": "autotask"
                        }
                    ],
                    "oauth2Provider": {
                        "tokenUrl": "https://api.hipchat.com/v2/oauth/token"
                    }
                }
            }