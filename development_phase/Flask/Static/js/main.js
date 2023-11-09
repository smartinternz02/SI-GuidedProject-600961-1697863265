$(document).ready(function () {
    $('#btn-predict').click(function () {
        // Create an object to store attribute values
        var attributes = {
            HighBP: $('#HighBP').val(),
            HighChol: $('#HighChol').val(),
            CholCheck: $('#CholCheck').val(),
            BMI: $('#BMI').val(),
            Smoker: $('#Smoker').val(),
            Stroke: $('#Stroke').val(),
            HeartDiseaseorAttack: $('#HeartDiseaseorAttack').val(),
            PhysActivity: $('#PhysActivity').val(),
            Fruits: $('#Fruits').val(),
            Veggies: $('#Veggies').val(),
            AnyHealthcare: $('#AnyHealthcare').val(),
            NoDocbcCost: $('#NoDocbcCost').val(),
            GenHlth: $('#GenHlth').val(),
            MentHlth: $('#MentHlth').val(),
            PhysHlth: $('#PhysHlth').val(),
            DiffWalk: $('#DiffWalk').val(),
            Sex: $('#Sex').val(),
            Age: $('#Age').val(),
            Education: $('#Education').val(),
            Income: $('#Income').val(),
            hvyAlcoholConsump: $('#hvyAlcoholConsump').val()
        };

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make a POST request to your Flask server
        $.ajax({
            type: 'POST',
            url: '/',
            data: attributes,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').text('Result: ' + data);
                console.log('Success!');
            },
        });
    });
});