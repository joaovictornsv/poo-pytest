import colander


class ProductSchema(colander.MappingSchema):
    name = colander.SchemaNode(typ=colander.String(), validator=colander.Length(3, 20))
    price = colander.SchemaNode(
        typ=colander.Float(), validator=colander.Range(0.1, 100)
    )
