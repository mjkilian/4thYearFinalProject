/**
 * Created by michael on 27/12/13.
 */

/**Ajax method for looking up an ingredient
 On success initialize a dialog containing info on the ingredient
 */
function lookup_ingredient(food_id,food_name){

    $.ajax({
        type: 'GET',
        url: '/search_ingredient/lookup/',
        data: {
            'food_id': food_id,
            'food_name': food_name
        },
        success: create_food_dialog,
        dataType: 'html'
  });
}
/**
 * As above but creates the modal with an 'add ingredient' button
 * @param food_id
 * @param food_name
 */
function lookup_ingredient_with_add(food_id,food_name){
    $.ajax({
        type: 'GET',
        url: '/search_ingredient/lookup/',
        data: {
            'food_id': food_id,
            'food_name': food_name,
            'add_ingredient_button':'True'
        },
        success: create_food_dialog,
        dataType: 'html'
  });
}


function create_food_dialog(data, textStatus, jqXHR){
    var modal_space = $('#ingredient_modal_space');
    modal_space.html(data); //render the modal contents in the page


     //make the initial serving visible
    var initial = $("#" + $("#serving_selector option:selected").val().toString());

    initial.css({'display': 'block'});


    //DEFINE MODAL BEHAVIOUR
    //now open the modal
    var modal = $('#ingredient_modal');
    modal.dialog({
        modal: true,
        width: '75%',
        buttons: {
            'Close': function () {
                $(this).dialog("close");
            }
        },
        position: {'my':'center','at':'center','of':window}
    });
    modal.css({'max-height':max_element_height(),'y-overflow':'scroll'});

    //handle a change to the selection
    $('#serving_selector').change(function () {

        //set all of the servings to be invisible
        $("#serving_selector option").each(function () {
            var id = "#" + $(this).val().toString();
            $(id).css('display', 'none');
        });


        //now make the selected serving visible
        $("#serving_selector option:selected").each(function () {
            var id = "#" + $(this).val().toString();
            $(id).css({'display': 'block', 'width': '100%'});
        });
    });

      //when closed we must completely destroy the dialog
    modal.on("dialogclose",function(){
        modal_space.empty();
        modal.dialog("destroy")
    });

    $(document).trigger("ing_lookup");

}