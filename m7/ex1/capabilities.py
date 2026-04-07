from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Capability contract for creatures that can perform healing actions."""
    @abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(ABC):
    """Capability contract for creatures that can transform and revert."""
    @abstractmethod
    def transform(self) -> str:
        """Apply transformed state and return the transform message."""
        ...

    @abstractmethod
    def revert(self) -> str:
        """Return to normal state and return the revert message."""
        ...
