library(shiny)

add_2 <- function(x) { x + 2 }

ui <- fluidPage(
  titlePanel("Add 2"),
  sidebarLayout(
    sidebarPanel( sliderInput("x", "Select x", min = 1, max = 50, value = 30) ),
    mainPanel( textOutput("x_updated") )
  )
)

server <- function(input, output) {
  # Add 2 to input$x, save as a reactive expression
  current_x        <- reactive({ add_2(input$x) })
  
  # Render the current result of input$x + 2
  output$x_updated <- renderText({ current_x() })
}

shinyApp(ui, server)