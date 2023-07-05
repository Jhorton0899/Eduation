import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.graph_objects as go

# Read the data
df = pd.read_excel("C:\\Users\\CollegeRanking.xlsx")

# Initialize the Dash app
app = dash.Dash(__name__)

# Set up the layout
app.layout = html.Div([
    html.H1("College Metrics Dashboard"),
    html.Div([
        html.Label('Country:', style={'marginRight': '10px'}),
        dcc.Dropdown(
            id='country-filter',
            options=[{'label': country, 'value': country} for country in df['Country'].unique()],
            multi=True,
            placeholder='Select country...',
            value=[]
        ),
        html.Label('State:', style={'marginRight': '10px'}),
        dcc.Dropdown(
            id='state-filter',
            options=[],
            multi=True,
            placeholder='Select state...',
            value=[]
        )
    ], style={'marginBottom': '20px', 'display': 'flex', 'justifyContent': 'space-between', 'maxWidth': '800px'}),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
    dcc.Graph(id='metrics-graph'),
    dcc.Graph(id='tuition-graph')
])

# Callback to update the state dropdown based on the selected country filter
@app.callback(
    dash.dependencies.Output('state-filter', 'options'),
    [dash.dependencies.Input('country-filter', 'value')]
)
def update_state_dropdown(selected_countries):
    # Filter the DataFrame based on the selected countries
    filtered_df = df[df['Country'].isin(selected_countries)]
    # Get the unique states for the selected countries
    state_options = [{'label': state, 'value': state} for state in filtered_df['State'].unique()]
    return state_options

# Callback to update the table based on the selected filters
@app.callback(
    dash.dependencies.Output('table', 'data'),
    [dash.dependencies.Input('country-filter', 'value'),
     dash.dependencies.Input('state-filter', 'value')]
)
def update_table_data(selected_countries, selected_states):
    # Apply filters progressively
    filtered_df = df[df['Country'].isin(selected_countries)]
    if selected_states:
        filtered_df = filtered_df[df['State'].isin(selected_states)]
    table_data = filtered_df.to_dict('records')
    return table_data

# Callback to update the metrics graph based on the selected filters
@app.callback(
    dash.dependencies.Output('metrics-graph', 'figure'),
    [dash.dependencies.Input('country-filter', 'value'),
     dash.dependencies.Input('state-filter', 'value')]
)
def update_metrics_graph(selected_countries, selected_states):
    # Apply filters progressively
    filtered_df = df[df['Country'].isin(selected_countries)]
    if selected_states:
        filtered_df = filtered_df[df['State'].isin(selected_states)]

    data = [
        go.Bar(x=filtered_df['Institution'], y=filtered_df['Education Rank'], name='Education Rank'),
        go.Bar(x=filtered_df['Institution'], y=filtered_df['Employability Rank'], name='Employability Rank'),
        go.Bar(x=filtered_df['Institution'], y=filtered_df['Research Rank'], name='Research Rank'),
        go.Bar(x=filtered_df['Institution'], y=filtered_df['Score'], name='Score')
    ]

    layout = go.Layout(
        title='College Metrics',
        xaxis={'title': 'Institution'},
        yaxis={'title': 'Metric Value'}
    )

    fig = go.Figure(data=data, layout=layout)
    return fig

# Callback to update the tuition graph based on the selected filters
@app.callback(
    dash.dependencies.Output('tuition-graph', 'figure'),
    [dash.dependencies.Input('country-filter', 'value'),
     dash.dependencies.Input('state-filter', 'value')]
)
def update_tuition_graph(selected_countries, selected_states):
    # Apply filters progressively
    filtered_df = df[df['Country'].isin(selected_countries)]
    if selected_states:
        filtered_df = filtered_df[df['State'].isin(selected_states)]

    fig = go.Figure(data=[go.Bar(x=filtered_df['Institution'], y=filtered_df['Tuition '])],
                    layout=go.Layout(title='Tuition Cost by Institution',
                                     xaxis={'title': 'Institution'},
                                     yaxis={'title': 'Tuition Cost'}))
    return fig

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

