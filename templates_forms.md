# Поля формы в одну колонку (без названий полей) но c placeholders

```
# templates/form/fields_in_one_column.html

<div class="fields_in_one_column">
        {% for field in form %}
        <div class="form-group">
            {{field.label_tag}}
            <div>{{field}}</div>
            <div class="error">{{field.errors}}</div>
        </div>
        {% endfor %}
        </div>
```
