from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_thingymajig

from . import base_thingymajig

class Gadget(base_thingymajig.BaseThingymajig):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Gadget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Gadget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Gadget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_thingymajig

        fields: Dict[str, Callable[[Any], None]] = {
            "maxRPM": lambda n : setattr(self, 'max_r_p_m', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def max_r_p_m(self,) -> Optional[int]:
        """
        Gets the maxRPM property value. The maxRPM property
        Returns: Optional[int]
        """
        return self._max_r_p_m
    
    @max_r_p_m.setter
    def max_r_p_m(self,value: Optional[int] = None) -> None:
        """
        Sets the maxRPM property value. The maxRPM property
        Args:
            value: Value to set for the max_r_p_m property.
        """
        self._max_r_p_m = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("maxRPM", self.max_r_p_m)
    

