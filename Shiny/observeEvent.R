library(shiny)
load(url("http://s3.amazonaws.com/assets.datacamp.com/production/course_4850/datasets/movies.Rdata"))

# UI
ui <- fluidPage(
  sidebarLayout(
    
    # Input
    sidebarPanel(
      
      # Numeric input for number of rows to show
      numericInput(inputId = "n_rows",
                   label = "How many rows do you want to see?",
                   value = 10),
      
      # Action button to show
      actionButton(inputId = "button", 
                   label = "Show")
      
    ),
    
    # Output:
    mainPanel(
      tableOutput(outputId = "datatable")
    )
  )
)

# Define server function required to create the scatterplot-
server <- function(input, output, session) {
  
  # Print a message to the console every time button is pressed
  observeEvent(input$button, {
    cat("Showing", input$n_rows, "rows\n")
  })
  # Take a reactive dependency on input$button, 
  # but not on any of the stuff inside the function
  df <- eventReactive(input$button, {
    head(movies, input$n_rows)
  })
  output$datatable <- renderTable({
    df()
  })
  
}

# Create a Shiny app object
shinyApp(ui = ui, server = server)