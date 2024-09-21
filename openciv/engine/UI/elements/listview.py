from __future__ import annotations
from ursina import Entity, color, mouse, Button, Tooltip, destroy
from typing import List


# TODO: replace all callable/handler logic in file with the ursina-provided/standard `Func` usage?


class ListView(Entity):
    def __init__(self, items: List[str], on_change: callable, title: str = "", item_tooltips: List[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.items = items
        self.on_change = on_change
        self.title = title
        self.selected_index = 0
        self.is_open = False
        self.text_entities = []
        self.dropdown = None
        self.title_text = None
        self.item_tooltips = item_tooltips

        self.selected_text = Button(
            text=f"{self.title}:     {self.items[self.selected_index]}",
            radius=-0.0,
            parent=self,
            scale=(10, 1),
            color=color.black,
            highlight_color=color.black,
        )

        # Create the dropdown list, initially hidden, with a black background
        self.dropdown = Entity(parent=self, enabled=False, position=(0, 0, -0.1))  # Move closer to the camera
        self.dropdown_background = Entity(
            parent=self.dropdown,
            model="quad",
            color=color.black,
            scale=(1.0, len(items) * 0.1 + 0.02),  # Adjusted scale to fit all items
            position=(
                0,
                -len(items) * 0.05 - 0.06,
                0.05,  # Move closer to the camera
            ),
        )
        self.highlight = Entity(
            parent=self.dropdown, model="quad", color=color.azure, scale=(5, 0.8), position=(0, 0, 0.04)
        )
        self._populate_list(items)

    def _populate_list(self, items):
        for i, item in enumerate(items):
            text_entity = Button(
                text=item if isinstance(item, object) else str(item),
                model="quad",
                radius=0.0,
                parent=self.dropdown,
                scale=(5, 0.8),
                position=(0, -i * 0.80 - 0.05, 0.05),  # Move closer to the camera
                color=color.black if i != self.selected_index else color.green,
                highlight_color=color.azure,
            )
            if self.has_tooltips():
                text_entity.tooltip = Tooltip(self.item_tooltips[i])
            self._register_item_input_handlers(i, text_entity)
            self.text_entities.append(text_entity)

        print(f'finished creating text entities: {self.text_entities}')
        self.highlight.position = self.text_entities[self.selected_index].position

    def _register_item_input_handlers(self, i: int, item_entity: Button):
        item_entity.on_click = self.create_click_handler(i)
        item_entity.on_mouse_enter = self.create_hover_handler(i)
        item_entity.on_mouse_exit = self.create_hover_end_handler(i)

    def create_click_handler(self, index):
        def handler():
            self.select_item(index)

        return handler

    def create_hover_handler(self, index):
        def handler():
            self.highlight.position = self.text_entities[index].position
            self.selected_index = index

            if self.has_tooltips():
                self.text_entities[index].tooltip.enabled = True

        return handler
    
    def create_hover_end_handler(self, index):
        def handler():
            if self.has_tooltips():
                self.text_entities[index].tooltip.enabled = False

        return handler

    def has_tooltips(self) -> bool:
        return self.item_tooltips is not None and isinstance(self.item_tooltips, list) and len(self.item_tooltips) > 0

    def calc_colors(self):
        for entity in self.text_entities:
            entity.color = color.black if self.selected_index != self.text_entities.index(entity) else color.green

    def toggle_dropdown(self):
        self.is_open = not self.is_open
        self.dropdown.enabled = self.is_open

    def input(self, key):
        if key == "left mouse down":
            if mouse.hovered_entity == self.selected_text:
                self.toggle_dropdown()

        if self.is_open:
            if key == "up arrow":
                self.selected_index = (self.selected_index - 1) % len(self.items)
                self.highlight.position = self.text_entities[self.selected_index].position
            elif key == "down arrow":
                self.selected_index = (self.selected_index + 1) % len(self.items)
                self.highlight.position = self.text_entities[self.selected_index].position
            elif key == "enter":
                self.select_item(self.selected_index)

    def select_item(self, index):
        self.selected_index = index
        self.selected_text.text = self.items[self.selected_index]
        self.calc_colors()
        self.toggle_dropdown()
        self.on_change(self.items[self.selected_index])

    @property
    def value(self):
        return self.items[self.selected_index]

    @value.setter
    def value(self, value):
        if value in self.items:
            self.selected_index = list(self.items.keys()).index(value)
            self.selected_text.text = value
            self.calc_colors()
        else:
            raise ValueError(f"Value {value} not in list of items")
        
    def update_items(self, items: List[str], item_tooltips: List[str] = None):
        print(f'updating listview "{self.title}" with new items: {items}')
        # reset selected index
        self.selected_index = 0
        self.selected_text = '...'

        # destroy old item entities and reinit the list
        for entity in self.text_entities:
            destroy(entity)
        self.text_entities = []

        # now repopulate with the new given items
        self.items = items
        self.item_tooltips = item_tooltips
        self._populate_list(items)