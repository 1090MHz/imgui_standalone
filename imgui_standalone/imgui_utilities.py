from pygame.key import get_pressed, key_code
from keyboard import is_pressed
from typing import Any

class ImGuiStandaloneUtilities:
    """Utilities."""

    values = {}

    @staticmethod
    def set_value(key: str, value: Any) -> None:
        """Save value."""
        ImGuiStandaloneUtilities.values[key] = value

    @staticmethod
    def get_value(key: str) -> Any:
        """Get value."""
        if key not in ImGuiStandaloneUtilities.values:
            return None
        return ImGuiStandaloneUtilities.values[key]

    @staticmethod
    def pressed(key: str) -> bool:
        """Is key pressed."""
        return get_pressed()[key_code(key)]

    @staticmethod
    def pressed_global(key: str) -> bool:
        """Is key pressed globally."""
        return is_pressed(key)
