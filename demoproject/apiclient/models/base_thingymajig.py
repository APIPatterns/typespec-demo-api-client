from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import color, manufacturer

class BaseThingymajig(Parsable):
    @property
    def color(self,) -> Optional[color.Color]:
        """
        Gets the color property value. The color property
        Returns: Optional[color.Color]
        """
        return self._color
    
    @color.setter
    def color(self,value: Optional[color.Color] = None) -> None:
        """
        Sets the color property value. The color property
        Args:
            value: Value to set for the color property.
        """
        self._color = value
    
    @property
    def created_on(self,) -> Optional[datetime]:
        """
        Gets the createdOn property value. Date and time that the resource was created
        Returns: Optional[datetime]
        """
        return self._created_on
    
    @created_on.setter
    def created_on(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdOn property value. Date and time that the resource was created
        Args:
            value: Value to set for the created_on property.
        """
        self._created_on = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseThingymajig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BaseThingymajig
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BaseThingymajig()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import color, manufacturer

        fields: Dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_enum_value(color.Color)),
            "createdOn": lambda n : setattr(self, 'created_on', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_object_value(manufacturer.Manufacturer)),
            "updatedOn": lambda n : setattr(self, 'updated_on', n.get_datetime_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def manufacturer(self,) -> Optional[manufacturer.Manufacturer]:
        """
        Gets the manufacturer property value. The manufacturer property
        Returns: Optional[manufacturer.Manufacturer]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[manufacturer.Manufacturer] = None) -> None:
        """
        Sets the manufacturer property value. The manufacturer property
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("color", self.color)
        writer.write_str_value("id", self.id)
        writer.write_object_value("manufacturer", self.manufacturer)
    
    @property
    def updated_on(self,) -> Optional[datetime]:
        """
        Gets the updatedOn property value. Date and time that the resource was last updated
        Returns: Optional[datetime]
        """
        return self._updated_on
    
    @updated_on.setter
    def updated_on(self,value: Optional[datetime] = None) -> None:
        """
        Sets the updatedOn property value. Date and time that the resource was last updated
        Args:
            value: Value to set for the updated_on property.
        """
        self._updated_on = value
    

