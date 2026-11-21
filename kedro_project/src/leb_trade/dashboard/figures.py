"""Plotly figure builders. Every function receives the trade table explicitly (`dff`)."""
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def create_time_series(dff, flow):
    #Filter dataframe according to trade flow
    dff = dff[dff['trade_flow'] == flow]
    
    #Style labels on time series:
    def get_text(value):
        '''
        Assign proper labels to points. If a trade value in a certain year is less than one billion,
        it will be written as follow: $123,45M. Otherwise, it will be written as follows: $123,45B, 
        and so on.
        '''
        if value < 10**6:
            text = '${}K'.format(np.round(value/(10**3), 2))
        elif value >=10**6 and value < 10**9:
            text = '${}M'.format(np.round(value/(10**6), 2))
        else:
            text = '${}B'.format(np.round(value/(10**9), 2))
        return text
    
    #Prepare dataframe
    dff = dff.groupby(['year'])['trade_value_usd'].sum().reset_index()
    
    #Create time series
    fig = go.Figure(
        data = go.Scatter(x = dff['year'],
                          y = dff['trade_value_usd'],
                          mode = 'lines+markers+text',
#                           text = dff['Value'],
                          text = [get_text(value) for value in dff['trade_value_usd']],
                          textposition = 'top center',
                          line = dict(color = 'crimson', width = 3),
                          hoverinfo = 'skip'),
        layout = go.Layout(template = 'simple_white',
                           font_family = 'Microsoft Yahei UI',
                           font_size = 13,
                           title = flow,
                           title_font_family = 'Microsoft Yahei UI',
                           title_font_size = 15,
                           title_font_color = 'black')
    )
    
    #Update axes and transition_duration
    fig.update_xaxes(tickfont = dict(family = 'Microsoft Yahei UI', size = 15))
    fig.update_yaxes(tickfont = dict(family = 'Microsoft Yahei UI', size = 15),
                     nticks = 6)
    
    return fig

#Example
#create_time_series('Export', dataframe[dataframe['HS2 Code'] == 15])


def create_products_treemap(dff, flow, year, depth):
    #Filter dataframe according to trade flow
    dff = dff[dff['trade_flow'] == flow]
    
    #Filter by year
    if year != 'All years': #A dropdown menu for years will have values 2011, 2012, ..., 2019, and 'All years'.
        dff = dff[dff['year'] == int(year)]
    else:
        dff = dff
        
    #Prepare dataframe
    hierarchy_levels = ['hs1_desc','hs2_desc','hs4_desc','hs6_desc']
    dff = dff.groupby(hierarchy_levels)['trade_value_usd'].sum().reset_index()
    
    #Create treemap
    fig = px.treemap(dff,
                     path = hierarchy_levels,
                     values = 'trade_value_usd',
                     color = hierarchy_levels[0],
                     title = '{}s'.format(flow),
                     maxdepth = int(depth))
    
    fig.update_traces(textinfo = 'label+value',
                      textfont = dict(family = 'Microsoft Yahei UI',
                                      size = 20,
                                      color = 'white'),
                      marker = dict(depthfade = True),
                     hovertemplate = '<b>%{label}</b><br><b>Share: </b> %{percentParent:.2f}')
    
    fig.update_layout(hoverlabel = dict(bgcolor = 'white', font_family = 'Microsoft Yahei UI'),
                      margin = dict(l=20,r=20,b=20),
                      title_font_size = 15,
                      title_font_family = 'Microsoft Yahei UI',
                      title_font_color = 'black')    
    
    return fig

#Example (depth takes the following options: 1,2,3 and 4)
#create_products_treemap('Export', 2019, 2)


def create_countries_treemap(dff, flow, year):
    #Filter dataframe according to trade flow
    dff = dff[dff['trade_flow'] == flow]
    
    #Filter by year
    if year != 'All years': #A dropdown menu for years will have values 2011, 2012, ..., 2019, and 'All years'.
        dff = dff[dff['year'] == int(year)]
        
    #Get title
    title = {'export':'Destinations', 'import':'Origins'}
        
    #Prepare dataframe
    hierarchy_levels = ['region','country']
    dff = dff.groupby(hierarchy_levels)['trade_value_usd'].sum().reset_index()
    
    #Create treemap
    fig = px.treemap(dff,
                     path = hierarchy_levels,
                     values = 'trade_value_usd',
                     color = hierarchy_levels[0],
                     title = title[flow])
    
    fig.update_traces(textinfo = 'label+value',
                      textfont = dict(family = 'Microsoft Yahei UI',
                                      size = 20,
                                      color = 'white'),
                      marker = dict(depthfade = True),
                      hovertemplate = '<b>%{label}</b><br><b>Share: </b> %{percentRoot:.2f}')
    
    fig.update_layout(hoverlabel = dict(bgcolor = 'white', font_family = 'Microsoft Yahei UI'),
                      margin = dict(l=20,r=20,b=20),
                      title_font_size = 15,
                      title_font_family = 'Microsoft Yahei UI',
                      title_font_color = 'black')    
    
    return fig

#Example
#create_countries_treemap('Import',2019)


def build_diff_treemap_products(dff, value, flow):        
    y1 = value[0]
    y2 = value[1]
    
    dff = dff[dff['trade_flow'] == flow]
    df1 = dff[dff['year'] == y1]
    df2 = dff[dff['year'] == y2]
    
    hierarchy_levels = ['hs1_desc','hs2_desc','hs4_desc','hs6_desc']
    
    df1 = df1.groupby(hierarchy_levels)['trade_value_usd'].sum().reset_index(name = 'Value at {}'.format(y1))
    df2 = df2.groupby(hierarchy_levels)['trade_value_usd'].sum().reset_index(name = 'Value at {}'.format(y2))
    
    diff = df1.merge(df2, how = 'outer', on = hierarchy_levels)
    
    diff = diff.fillna(0)
    
    diff['Difference'] = diff['Value at {}'.format(y2)] - diff['Value at {}'.format(y1)]
    diff['Absolute'] = diff['Difference'].apply(lambda x: abs(x))
    
    diff = diff[diff['Absolute'] > 0]
    
    title = '{} Difference between {} and {} - Products'.format(flow, y1, y2)
    
    fig = px.treemap(diff,
                     path = hierarchy_levels,
                     values = 'Absolute',
                     color = 'Difference',
                     color_continuous_scale = 'RdBu',
                     color_continuous_midpoint = 0,
                     title = title,
                     maxdepth = 2)
    
    fig.update_traces(textinfo = 'label+value',
                      textfont = dict(family = 'Microsoft Yahei UI',
                                      size = 20),
                      marker = dict(depthfade = True),
                      hovertemplate = '<b>%{label}</b><br><b>Difference: </b>$%{color:.2f}<br>')
    
    fig.update_layout(hoverlabel = dict(bgcolor = 'white', font_family = 'Microsoft Yahei UI'),
                      margin = dict(l=20,r=20,b=20),
                      transition_duration = 500,
                      title_font_size = 15,
                      title_font_family = 'Microsoft Yahei UI',
                      title_font_color = 'black')  
    return fig

#Example
#build_diff_treemap_products([2014,2019], 'Export')


def build_diff_treemap_countries(dff, value, flow):
    y1 = value[0]
    y2 = value[1]
    
    dff = dff[dff['trade_flow'] == flow]
    df1 = dff[dff['year'] == y1]
    df2 = dff[dff['year'] == y2]
    
    hierarchy_levels = ['region','country']
    
    df1 = df1.groupby(hierarchy_levels)['trade_value_usd'].sum().reset_index(name = 'Value at {}'.format(y1))
    df2 = df2.groupby(hierarchy_levels)['trade_value_usd'].sum().reset_index(name = 'Value at {}'.format(y2))
    
    diff = df1.merge(df2, how = 'inner', on = hierarchy_levels)
    
    diff = diff.fillna(0)
    
    diff['Difference'] = diff['Value at {}'.format(y2)] - diff['Value at {}'.format(y1)]
    diff['Absolute'] = abs(diff['Difference'])
    
    diff = diff[diff['Absolute'] > 0]
    
    title = '{} Difference between {} and {} - Countries'.format(flow, y1, y2)
    
    fig = px.treemap(diff,
                     path = hierarchy_levels,
                     values = 'Absolute',
                     color = 'Difference',
                     color_continuous_scale = 'RdBu',
                     color_continuous_midpoint = 0,
                     title = title)
    fig.update_traces(textinfo = 'label+value',
                      textfont = dict(family = 'Microsoft Yahei UI',
                                      size = 20),
                      marker = dict(depthfade = True),
                      hovertemplate = '<b>%{label}</b><br><b>Difference: </b>$%{color:.2f}<br>')
    
    fig.update_layout(hoverlabel = dict(bgcolor = 'white', font_family = 'Microsoft Yahei UI'),
                      margin = dict(l=20,r=20,b=20),
                      transition_duration = 500,
                      title_font_size = 15,
                      title_font_family = 'Microsoft Yahei UI',
                      title_font_color = 'black')  
    return fig

#Example
#build_diff_treemap_countries([2014,2019],'Export')
