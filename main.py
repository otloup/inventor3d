import lib3mf
import tabulate

wrapper = lib3mf.get_wrapper()

model = wrapper.CreateModel()

if model is not None and isinstance(model, lib3mf.Model):
    reader = model.QueryReader(ReaderClass="3mf")
    reader.ReadFromFile("resources/example.3mf")
    meta = model.GetMetaDataGroup()
    meta_table = [["name", "key", "type", "value"]]

    if isinstance(meta, lib3mf.MetaDataGroup):
        for index in range(meta.GetMetaDataCount()):
            data = meta.GetMetaData(index)
            name = data.GetName()
            key = data.GetKey()
            type = data.GetType()
            value = data.GetValue()
            meta_table.append([name, key, type, value])

        print(tabulate.tabulate(meta_table, headers="firstrow"))
