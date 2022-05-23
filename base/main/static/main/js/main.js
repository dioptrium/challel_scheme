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
      
    
        /* код сохранения в csv - не работающий (выключен)
        output_separator     : ',',         // ',' 'json', 'array' or separator (e.g. ';')
        output_ignoreColumns : [],         // columns to ignore [0, 1,... ] (zero-based index)
        output_hiddenColumns : false,       // include hidden columns in the output
        output_includeFooter : true,        // include footer rows in the output
        output_includeHeader : true,        // include header rows in the output
        output_headerRows    : false,       // output all header rows (if multiple rows)
        output_dataAttrib    : 'data-name', // data-attribute containing alternate cell text
        output_delivery      : 'd',         // (p)opup, (d)ownload
        output_saveRows      : 'f',         // (a)ll, (v)isible, (f)iltered, jQuery filter selector (string only) or filter function
        output_duplicateSpans: true,        // duplicate output data in tbody colspan/rowspan
        output_replaceQuote  : '\u201c;',   // change quote to left double quote
        output_includeHTML   : true,        // output includes all cell HTML (except the header cells)
        output_trimSpaces    : false,       // remove extra white-space characters from beginning & end
        output_wrapQuotes    : true,       // wrap every cell output in quotes
        output_popupStyle    : 'width=580,height=310',
        output_saveFileName  : 'mytable.xls',
        */
      }

      
    })
    /*
   .tablesorterPager({
  
      // target the pager markup - see the HTML block below
      container: $(".ts-pager"),
  
      // target the pager page select dropdown - choose a page
      cssGoto  : ".pagenum",
  
      // remove rows from the table to speed up the sort of large tables.
      // setting this to false, only hides the non-visible rows; needed if you plan to add/remove rows with the pager enabled.
      removeRows: false,
  
      // output string - default is '{page}/{totalPages}';
      // possible variables: {page}, {totalPages}, {filteredPages}, {startRow}, {endRow}, {filteredRows} and {totalRows}
      output: '{startRow} - {endRow} / {filteredRows} ({totalRows})'
  
    });
    */
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

  
  
/*$(document).ready(function() {
  var $elFrom = $('td[id="from1"]').value;
  $('td[id="in"]').text($elFrom);
  });
  
  const addMoreBtn =  document.getElementById('add-more')
    addMoreBtn.addEventListener('click', add_new_form)
    function add_new_form(event) {
      if (event) {
          event.preventDefault()
      }
      const formCopyTarget = document.getElementById('clone-form-list')
      const emptyFormEl = document.getElementById('empty-form').cloneNode(true)
      emptyFormEl.setAttribute('class', 'clone-form')
      formCopyTarget.append(emptyFormEl)
    }*/
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
      


      
      /**/