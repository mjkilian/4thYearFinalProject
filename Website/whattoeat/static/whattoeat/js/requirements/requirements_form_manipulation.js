/**
 * Created by michael on 15/01/14.
 * Adapted from http://stellarchariot.com/blog/2011/02/dynamically-add-form-to-formset-using-javascript-and-django/
 */

$(document).ready(function () {
    // Code adapted from http://djangosnippets.org/snippets/1389/
    function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\\d+-)');
        var replacement = prefix + '-' + ndx + '-';
        if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
        replacement));
        if (el.id) el.id = el.id.replace(id_regex, replacement);
        if (el.name) el.name = el.name.replace(id_regex, replacement);
    }

    function deleteForm(btn, prefix) {
        var form_id = "."+prefix + "_space";
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        if (formCount > 1) {
            // Delete the item/form
            $(btn).parents(form_id).remove();
            var forms = $(form_id); // Get all the forms
            // Update the total number of forms (1 less than before)
            var formCount = forms.length;
            $('#id_' + prefix + '-TOTAL_FORMS').val(formCount);

            // Go through the forms and set their indices, names and IDs
            for (i = 0; i < formCount; i++) {
                $(forms.get(i)).children().children().each(
                    updateElementIndex(this, prefix, i)
                );
            }
        } // End if
        return false;
    }

    function addForm(btn, prefix) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        var form_id = "." + prefix  + "_space"
            // Clone a form (without event handlers) from the first form
            var row = $(form_id + ":first").clone(false).get(0);
            // Insert it after the last form
            $(row).removeAttr('id').hide().insertAfter(form_id+":last").slideDown(300);

            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            $(".errorlist", row).remove();
            $(row).children().removeClass("error");

            // Relabel or rename all the relevant bits
            $(row).children().children().each(function () {
                updateElementIndex(this, prefix, formCount);
                $(this).val("");
            });

            // Add an event handler for the delete item/form link
            $(row).find(".delete_" + prefix).click(function () {
                return deleteForm(this, prefix);
            });
            // Update the total form count
            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);
        return false;
    }
    // Register the click event handlers
    $("#add_definite").click(function () {
        return addForm(this, "definite");
    });

    $(".delete_definite").click(function () {
        return deleteForm(this, "definite");
    });

    $("#add_restricted").click(function () {
        return addForm(this, "restricted");
    });

    $(".delete_restricted").click(function () {
        return deleteForm(this, "restricted");
    });

    function removeExtraForms(prefix){
        /*By default django formsets are rendered with an extra empty form,
         This method overrides that behavior if some data is already rendered
         */
        var form_count_input = $('#id_' + prefix + '-TOTAL_FORMS');
        var formCount = parseInt(form_count_input.val());
        var form_id = "." + prefix + "_space";
        if(formCount > 1){
            //remove last form
            $(form_id + ":last").remove();
            //decrement form count
            form_count_input.val(form_count_input.val() - 1);
        }
    }
    removeExtraForms("definite");
    removeExtraForms("restricted");
    console.log($('html').html());

});