from __future__ import annotations
from openciv.engine.UI.menu import Menu


class GameConfig(Menu):
    """
    TODO this will probably be a different kind of menu, or at least heavily customized...
    either a tabbed_menu, or a "staged" tab menu?
    """
    def __init__(self, game_manager, *args, **kwargs):
        # self.panel = None
        super().__init__(parent=game_manager, title='Setup New Game', *args, **kwargs)
        self._civ_data = self.parent().game_data()['civilization']
        self._civ_identifier_dict = {}
        self._playable_civs = []
        self._leaders = []
        self._civ_descriptions = []
        self._leader_descriptions = []
        self._civ_list_view = None
        self._leader_list_view = None

    def get_leaders_for_civ(self, civ_name: str):
        selected_civ_key = self._civ_identifier_dict[civ_name]
        civ_leaders = self._civ_data[selected_civ_key]['leaders']
        return [leader['name'] for leader in civ_leaders.values()]

    def setup_content(self):
        for civ_key, civ_data in self._civ_data.items():
            civ_name = civ_data['name']
            self._playable_civs.append(civ_name)
            self._civ_descriptions.append(civ_data['description'])
            # a dict of civilation names back to their keys in the main dictionary for quicker retrieval via name
            self._civ_identifier_dict[civ_name] = civ_key

        self._civ_list_view = self.ListView(
                self._playable_civs,
                position=(-0.5, 0),
                parent=self.panel,
                title="Civilization",
                item_tooltips=self._civ_descriptions,
                on_change=lambda selection: self._leader_list_view.update_items(self.get_leaders_for_civ(selection)))
        
        self._leader_list_view = self.ListView(
            ['Select civilization...'],
            parent=self.panel,
            title='Leader',
            on_change=lambda selection: print(selection)
        )
        
        return [
            #TODO update 'on_change' to point to `update_selections`
            self.Text("<pre>Configure your game</pre>", size=0.016),
            self.ListView(
                ["Small", "Medium", "Large", "Huge"],
                parent=self.panel,
                title="World Size",
                on_change=lambda x: print(x),  # noqa
            ),
            self._civ_list_view,
            self._leader_list_view,
            # TODO add play & reset button(s)...
            self.BackButton()
        ]
