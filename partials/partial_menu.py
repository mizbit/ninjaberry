#!/usr/bin/env python3
# coding=utf8

import time

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from partials.partial import Partial

from ui.ui_animation import UIAnimation
from ui.ui_button import UIButton
from ui.ui_label import UILabel
from ui.ui_line import UILine
from ui.ui_list import UIList

class PartialMenu(Partial):
    def __init__(self, resources, event_handler):
        self._resources = resources
        self._event_handler = event_handler
        self._partial = {
            'id': 'menu',
            'horizontal': [
                {
                    'id': 'button_menu_wifi',
                    'element': UIButton(
                        resources = { 'font': self._resources['fonts']['fa_solid'] },
                        event_handler = (lambda event, next, payload={}: self._event_handler(element_id='button_menu_wifi', event=event, next=next, payload=payload)),
                        position = [0, 0],
                        size = [15, 14],
                        label = chr(0xf1eb)
                    )
                },
                {
                    'id': 'button_menu_bt',
                    'element': UIButton(
                        resources = { 'font': self._resources['fonts']['fa_brands'] },
                        event_handler = (lambda event, next, payload={}: self._event_handler(element_id='button_menu_bt', event=event, next=next, payload=payload)),
                        position = [16, 0],
                        size = [15, 14],
                        label = chr(0xf294)
                    )
                },
                {
                    'id': 'button_menu_eth',
                    'element': UIButton(
                        resources = { 'font': self._resources['fonts']['fa_solid'] },
                        event_handler = (lambda event, next, payload={}: self._event_handler(element_id='button_menu_eth', event=event, next=next, payload=payload)),
                        position = [32, 0],
                        size = [15, 14],
                        label = chr(0xf796)
                    )
                },
                {
                    'id': 'button_menu_settings',
                    'element': UIButton(
                        resources = { 'font': self._resources['fonts']['fa_solid'] },
                        event_handler = (lambda event, next, payload={}: self._event_handler(element_id='button_menu_settings', event=event, next=next, payload=payload)),
                        position = [48, 0],
                        size = [15, 14],
                        label = chr(0xf013)
                    )
                },
                {
                    'id': 'line_menu',
                    'element': UILine(
                        resources = {},
                        position = [0, 15, self._resources['display']['width'], 15],
                        size = 1,
                        fill = 255
                    )
                }
            ]
        }

    def event(self, element_id, event, next, payload={}):
        navigate_to = None

        if event == 'clicked':
            if element_id == 'button_menu_wifi':
                navigate_to = 'wifi'
            elif element_id == 'button_menu_bt':
                navigate_to = 'bt'
            elif element_id == 'button_menu_eth':
                navigate_to = 'eth'
            elif element_id == 'button_menu_settings':
                navigate_to = 'settings'

        if navigate_to != None:
            return self._event_handler(element_id=element_id, event='navigate', next=None, payload={ 'to': navigate_to })

        return True
