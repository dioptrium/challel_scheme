$(function() {

      
    // NOTE: $.tablesorter.themes.bootstrap is ALREADY INCLUDED in the jquery.tablesorter.widgets.js
    // file; it is included here to show how you can modify the default classes
    $.tablesorter.themes.bootstrap = {
      // these classes are added to the table. To see other table classes available,
      // look here: http://getbootstrap.com/css/#tables
      table        : 'table table-bordered table-striped',
      caption      : 'caption',
      // header class names
      header       : 'bootstrap-header', // give the header a gradient background (theme.bootstrap_2.css)
      sortNone     : '',
      sortAsc      : '',
      sortDesc     : '',
      active       : '', // applied when column is sorted
      hover        : '', // custom css required - a defined bootstrap style may not override other classes
      // icon class names
      icons        : '', // add "bootstrap-icon-white" to make them white; this icon class is added to the <i> in the header
      iconSortNone : 'bootstrap-icon-unsorted', // class name added to icon when column is not sorted
      iconSortAsc  : 'glyphicon glyphicon-chevron-up', // class name added to icon when column has ascending sort
      iconSortDesc : 'glyphicon glyphicon-chevron-down', // class name added to icon when column has descending sort
      filterRow    : '', // filter row class; use widgetOptions.filter_cssFilter for the input/select element
      footerRow    : '',
      footerCells  : '',
      even         : '', // even row zebra striping
      odd          : ''  // odd row zebra striping
    };
  
    
  
    // call the tablesorter plugin and apply the uitheme widget
    $("table").tablesorter({
      // this will apply the bootstrap theme if "uitheme" widget is included
      // the widgetOptions.uitheme is no longer required to be set
      theme : "bootstrap",
  
      widthFixed: false,
  
      headerTemplate : '{content} {icon}', // new in v2.7. Needed to add the bootstrap icon!
  
      // widget code contained in the jquery.tablesorter.widgets.js file
      // use the zebra stripe widget if you plan on hiding any rows (filter widget)
      widgets : [ "uitheme", "filter", "columns", "zebra", "print", "resizable", "stikyHeaders"/*"columnSelector", "output"*/],
  
      widgetOptions : {
        // using the default zebra striping class name, so it actually isn't included in the theme variable above
        // this is ONLY needed for bootstrap theming if you are using the filter widget, because rows are hidden
        zebra : ["even", "odd"],
  
        // class names added to columns when sorted
        columns: [ "primary", "secondary", "tertiary" ],
  
        // reset filters button
        filter_reset : ".reset",
  
        // extra css class name (string or array) added to the filter element (input or select)
        filter_cssFilter: "form-control",

        // resizable table column
        resizable: true,
        // These are the default column widths which are used when the table is
        // initialized or resizing is reset; note that the "Age" column is not
        // resizable, but the width can still be set to 40px here
        resizable_widths : [  ],
  
        // set the uitheme widget to use the bootstrap theme class names
        // this is no longer required, if theme is set
        // ,uitheme : "bootstrap"
      

      print_title      : '',          // this option > caption > table id > "table"
      print_dataAttrib : 'data-name', // header attrib containing modified header name
      print_rows       : 'f',         // (a)ll, (v)isible, (f)iltered, or custom css selector
      print_columns    : 's',         // (a)ll, (v)isible or (s)elected (columnSelector widget)
      print_extraCSS   : '',          // add any extra css definitions for the popup window here
      print_styleSheet : '../css/theme.blue.css', // add the url of your print stylesheet
      print_now        : true,        // Open the print dialog immediately if true
      
      }

      
    })

    $('.print').click(function() {
      $('.tablesorter').trigger('printTable');
    });
});

//Export file in xls
function exportTableToExcel(tableID, filename = ''){
  var downloadLink;
  var dataType = 'application/vnd.ms-excel';
  var tableSelect = document.getElementById(tableID);
  var tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');
  
  // Specify file name
  filename = filename?filename+'.xls':'excel_data.xls';
  
  // Create download link element
  downloadLink = document.createElement("a");
  
  document.body.appendChild(downloadLink);
  
  if(navigator.msSaveOrOpenBlob){
      var blob = new Blob(['\ufeff', tableHTML], {
          type: dataType
      });
      navigator.msSaveOrOpenBlob( blob, filename);
  }else{
      // Create a link to the file
      downloadLink.href = 'data:' + dataType + ', ' + tableHTML;
  
      // Setting the file name
      downloadLink.download = filename;
      
      //triggering the function
      downloadLink.click();
  }
}

  $(document).ready(function()  {
    $("#hidebutton").hide('slow').show('slow');
  });

  /*Добавление строки оборудования и спецификации*/
    
  $(document).ready(function() {
      $('.add-item').click(function(ev) {
          ev.preventDefault();
          var count = $('#items-form-container').children().length;
          var tmplMarkup = $('#item-template').html();
          var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
          $('div#items-form-container').append(compiledTmpl);
          
          // update form count
          $('#id_locationcon-TOTAL_FORMS').attr('value', count+1);
          $('#id_specificationcon-TOTAL_FORMS').attr('value', count+1);
          // some animate to scroll to view our new form
          $('html, body').animate({
            scrollTop: $("#add-item-button").position().top-200
          }, 800);
        });
      });
      

