from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models import gadget

class GadgetsResponse(Parsable):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GadgetsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GadgetsResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GadgetsResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..models import gadget

        fields: Dict[str, Callable[[Any], None]] = {
            "nextLink": lambda n : setattr(self, 'next_link', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(gadget.Gadget)),
        }
        return fields
    
    @property
    def next_link(self,) -> Optional[str]:
        """
        Gets the nextLink property value. A link to the next page of results if present.
        Returns: Optional[str]
        """
        return self._next_link
    
    @next_link.setter
    def next_link(self,value: Optional[str] = None) -> None:
        """
        Sets the nextLink property value. A link to the next page of results if present.
        Args:
            value: Value to set for the next_link property.
        """
        self._next_link = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("nextLink", self.next_link)
        writer.write_collection_of_object_values("value", self.value)
    
    @property
    def value(self,) -> Optional[List[gadget.Gadget]]:
        """
        Gets the value property value. List of elements
        Returns: Optional[List[gadget.Gadget]]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[List[gadget.Gadget]] = None) -> None:
        """
        Sets the value property value. List of elements
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

