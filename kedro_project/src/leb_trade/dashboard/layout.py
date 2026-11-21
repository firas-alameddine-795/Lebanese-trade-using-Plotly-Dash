"""Static page layouts: sidebar, home / HS / user-guide pages and the four dashboard tabs."""
import dash_bootstrap_components as dbc
from dash import dcc, html

from . import figures


#CSS style for paragraphs
PARAGRAPH_STYLE = {'fontSize':'15px',
                   'text-align':'justify',
                   'text-justify':'inter-word',
                   'padding-right':'15rem'}


### Page 1: Home
home = html.Div([
    dbc.Row(html.H1('Home', className = 'display-1', style = {'padding-left':'15px'})),
    html.Hr(),
    
    dbc.Row(html.H4('Abstract', className = 'display-4', style = {'padding-left':'15px'})),
    html.P("""Despite the fact that the free fall of the Lebanese currency exchange rate, has had severe negative
    impact on the economy, illustrated by the sharp increase in prices, this free fall could create an opportunity
    for the Lebanese industry to evolve and gain new momentum. In fact, the sharp increase of prices of imported
    products makes it almost impossible for ordinary consumers to buy as they used to do prior to the crisis, hence
    the need for cheaper local alternative goods (many of which are virtually inexistent).
    Also, the decrease of production costs (in US$) of Lebanese goods provides an opportunity for manufacturers
    to increase their level of exports to foreign markets, an act which would help eliminate gradually trade deficit
    as new markets start importing cheaper Lebanese goods compared to similar goods’ prices in these markets.""",
          style = PARAGRAPH_STYLE),
    
    html.Br(),
    
    dbc.Row(html.H4('Project', className = 'display-4', style = {'padding-left':'15px'})),
    html.P([
        html.P("""The goal of this capstone project is to support knowledge acquired throughout my MSBA by getting 
        hand-on work experience with public data. The choice of such a topic is intentional: For it helps me hone my 
        newly acquired skills in data analytics. Accordingly, the progression of my capstone will be divided into the
        following milestones:"""),
        dbc.Row(''),
        html.B('Milestone 1: Use and analyze data in Lebanese Industry and Commerce'),
        html.P("""In the First part, the focus will be on the collection of Lebanese Customs data, as well as 
        international trade data available via official platforms, namely World Bank, WTO and WCO. The aim is to add
        my contribution in terms of reporting methodology, metrics, evaluation, use of visualization, coding 
        automation and recommendations given."""),
        dbc.Row(''),
        html.B('Milestone 2: Data Overview'),
        html.P("""The second part is more informative and will go through an overview of the data tools and sources,
        highlighting both strong and weak points."""),
        html.P(html.I('Tools to be used: Python (main work), Tableau (investigative work).')),
        dbc.Row(''),
        html.B('Milestone 3: Data Driven Answers'),
        html.P('Finally, the third part is meant to provide answers for the following questions:'),
        html.P('''1- What are the main countries Lebanon is dealing with for each import/export category? How did it 
        evolve with time from 2011 to 2019?''', style = {'padding-left':'30px'}),
        html.P("""2- What are the export verticals that are growing in Lebanon and what are the ones shrinking?""",
               style = {'padding-left':'30px'}),
        html.P("""3- How does our pricing per ton for exports compare with the one from other countries?""", 
               style = {'padding-left':'30px'}),
        html.P("""4- Is the pricing per ton for our imports competitive? Are neighboring countries (such as Jordan)
        getting better deals?""", style = {'padding-left':'30px'}),
        html.P("""5- What are the export verticals that exist in Lebanon and that have a potential for growth as 
        other comparable countries were able to grow in the past three years?""", style = {'padding-left':'30px'})
    ], style = PARAGRAPH_STYLE),
])


### Page 2: Harmonized System

harmonized_system = html.Div([
    dbc.Row(html.H1('Harmonized System', className = 'display-1', style = {'padding-left':'15px'})),
    html.Hr(),
    
    dbc.Row(html.H4('Introduction', className ='display-4', style = {'padding-left':'15px'})),
    html.P(html.I(['"With over US$ 15 trillion worth of goods moving around the world, ', 
           html.B('how do you know what is crossing your border? '),
            """This is the issue that the Harmonized Commodity description and Coding System (Commonly known as the
            Harmonized System or the HS) is designed to adress. It is a nomenclature which enables all goods moving
            across borders to be assigned to a class in a uniform manner all over the world. As of 2018. It is used as
            the basis for Customs tariffs and for the compilation of international trade statistics." """], 
          ),style = PARAGRAPH_STYLE),
    
    html.P([html.I('''"The HS is one of the most successful instruments developed by the World Customs Organization (WCO) 
        it adresses a fundamental need of governments: the ability to categorize what is being traded. This enables 
        both decisions on immediate actions for specific goods (duty collections, restrictions or controls, international
        trade regulations) and the use of the collated information to underpin economic and trade related policies
        and planning."'''), """ - World Customs Organization. The Harmonized System: A Universal Language for 
        International Trade. """], style = PARAGRAPH_STYLE),
    
    html.Br(),
    
    dbc.Row(html.H4('Definition',  className ='display-4', style = {'padding-left':'15px'})),
    html.P(["""The Harmonized Commodity Description and Coding System (or simply the Harmonized System or the HS)
    is - as the name implies - a system of codes and names used to categorize and label all sorts of products
    traded around the globe."""], style = PARAGRAPH_STYLE), 
    html.P(["""Since the 1900's, the world has been witnessing an enormous growth in the complexity and range of
    traded products, and in the frequency of trade between parties. With this expansion, the demand of a highly
    structured system aimed at providing accurate information on international trade and detailed descriptions of 
    goods has grown. After several attempts to regularize trade globally, the HS came to existence in 1983 and was put into
    action in 1988. The WCO describes the HS as one of its most successful instruments, because it has been accurately 
    adressing a fundamental need of governments: the categorization of what is traded. As of 2018, the HS is used as 
    a basis for numerous government regulations such as customs tariffs, duty collection, freight taxes, monitoring 
    of controlled goods, and the compilation of international trade statistics, by more than 180 members of the WCO, 
    most of which are developing countries which depend on customs duties for national revenues."""], 
           style = PARAGRAPH_STYLE),
    
    html.P(["""Since its inception, the HS has been revised frequently to overcome disputes rising between trade 
    parties over the right definitions of products, and to stay up to date with new products entering the market 
    and imposing new trade patterns over time. The latest version of the HS was established in 2017, and a newer
    one will take its place in 2022."""],style = PARAGRAPH_STYLE),
    
    html.Br(),
    
    dbc.Row(html.H4('Structure', className = 'display-4', style = {'padding-left':'15px'})),
    html.P(['''The HS uses a hierarchy to categorize traded goods into certain groups. All goods are grouped into 21
    ''', html.I(' Sections '), 'that are subdivided into 96', html.I(' Chapters .'),
    '''Sections and chapters provide broad definitions of products for ease of access and understanding. Furthermore, 
    chapters are subdivided into more than 1200''', html.I(' Headings '), """which are further subdivided into more 
    than 5200""", html.I(' Sub-Headings'), """, to provide a more detailed and accurate decriptions of products."""],
           style = PARAGRAPH_STYLE),
    
    html.P(['''Each product in the Harmonized System is given a 6-digits code. Every member of the WCO 
    (i.e. using the HS) is allowed to do further dissections of product categories, by adding as many digits as they
    feel they need: products with more than 6 digits are said to be at the national tariff-level. To read a product’s
    code, one must bare in mind that the code is actually an assembling of three 2-digits codes: the first couple of
    digits corresponds to chapters (and they go from 1 to 97 with the exclusion of chapter 77), and the second and
    third couples are assigned to headings and sub-headings respectively (coding of headings depends on how
    many headings there is in each chapter. The same analogy is applied to sub-headings relative to headings).'''], 
           style = PARAGRAPH_STYLE),
    
    dbc.Row([
        dbc.Col(
            html.P(['''The photo on the left is an example of what is mentioned right above. Consider the case of
            product 100630: the first couple of digits is 10, referring to chapter 10 in the HS. The second 
            couple is 06, which leads to heading 06 in chapter 10. The third couple is 30, which refers
            to subheading 30 in heading 06. Again, ach section is a list of chapters containing products 
            that are of similar complexity to produce.'''], style = PARAGRAPH_STYLE), width = 8
        ),
        
        dbc.Col(dbc.Card([
            dbc.CardImg(src = '/assets/hs.png', style = {'height':'160px'}),
            dbc.CardFooter('An example of how products are categorized in the HS')
        ]), width = 4)
    ], style = PARAGRAPH_STYLE),
    
    html.Br(),
    
])


### Page 3: User Guide

def build_userguide(df):
    """User-guide page; it embeds live example charts, hence needs the trade table."""
    return html.Div([
        dbc.Row(html.H1('User Guide', className = 'display-1', style = {'padding-left':'15px'})),
        html.Hr(),
    
        dbc.Row(html.H4('Introduction', className = 'display-4', style = {'padding-left':'15px'})),
        html.P("""Here, I briefly explain how the dash apps work, by showcasing one component at a time. There are four dash
        apps, each of which has its own purpose, even though they look very similar. Dash App 1 illustrates two treemaps to 
        distribute trade values by products (Imports and Exports) and by countries (Origins and Destinations), and a line
        chart to look at these trade values over time. Mainly, a user would interact with Dash App 1 to observe trade patterns
        of each product between Lebanon and corresponding partners. Dash App 2 works similarly, but its purpose is to observe
        a trade portfolio of products between Lebanon and a certain partner (the other way around, kind of). Dash Apps 3 and 4
        are similar to Dash Apps 1 and 2 (respectively) but they show trade growth change instead of trade values.
    
        Firstly, I define the dropdown menus. Then I explain each figure: What it is, How it works, How to read it and infer
        from it. Lastly, I describe the connection between the figures, by describing how interaction between figures 
        works.""", style = PARAGRAPH_STYLE),
    
        html.Br(),
    
        dbc.Row(html.H4('Dropdown Menus', className = 'display-4', style = {'padding-left':'15px'})),
        dbc.Row([
            dbc.Col(html.P(
                [html.P(["""These dropdown menus are here to filter the database behind the dashoards. They represent the
                categorical fields defining each trade value in the database: commodity description, year and trade flow. 
                The first dropdown menu """, html.B('Select Depth Level '), """implies how deep the treemaps shall be.
                Its first value 1 distributes trade values by sections (first level of granularity in the HS), 
                whereas its second value 2 distributes trade values by sections then chapters 
                (first two levels of granularity in the HS). 

                Toggling between these values change the """, html.Code('maxdepth = ', style = {'fontSize':'15px'}),
                'property in the ' , html.Code('px.treemap() ', style = {'fontSize':'15px'}), """functions. 

                By clicking on the treemap and setting the depth value to 2, the treemap automatically digs into
                the next level. For example, when the user selects a chapter, the treemap immediately shows the headings
                underneath that chapter."""]),
            
                html.P(['The two other Dropdown Menus ', html.B('Select Trade Flow '), 'and ', html.B('Select Year '),
                'filter the dataframe by trade flow and year. The value', html.I(' All years '),
                """in the third menu sums trade values for the whole period between 2011 and 2019.
                The Menus typically activate callbacks each time a value is changed, which hinders time efficiency.
            
            
                Therefore, a """, dbc.Button('Submit', color = 'success', style = {'height':'20px'},
                                             size = 'sm'),
                """ is added to hold these callbacks from firing every single time. A user would then select a filtering
                combination and click on the button to find results he is looking for."""]),
             
                 html.P(["""The Range Slider for years is specifically added for Dash Apps 3 and 4, which illustrate the
                 growth change of trade values between two years, by products and by countries."""])
        
            ]), width = 8),
        
            dbc.Col(dbc.Card([
                dbc.Label('Select Depth Level'),
                dbc.Select(options=[{'label': str(i), 'value': i} for i in [1, 2]],
                           value=1, size='lg'),

                dbc.Label('Select Trade Flow'),
                dbc.Select(options=[{'label': flow, 'value': flow} for flow in ['export', 'import']],
                           value='export', size='lg'),

                dbc.Label('Select Year'),
                dbc.Select(options=[{'label': 'All years', 'value': 'All years'}] +
                           [{'label': str(year), 'value': year} for year in list(reversed(range(2011, 2020)))],
                           value=1, size='lg'),

                dbc.Label('Select Range of Years'),
                dcc.RangeSlider(marks={year: {'label': str(year)} for year in range(2011, 2020)},
                                value=[2014, 2019], min=2011, max=2019, pushable=True, step=1)
            ], body=True), width=4)
        ], style=PARAGRAPH_STYLE),
    
        html.Br(),
    
        dbc.Row(html.H4('Treemaps', className = 'display-4', style = {'padding-left':'15px'})),
        dbc.Row([
            dbc.Col(dbc.Card(
            dbc.Row([
                dbc.Col(dcc.Loading(dcc.Graph(figure = figures.create_products_treemap(df, 'export', 'All years', '2'))), width = 6),
                dbc.Col(dcc.Loading(dcc.Graph(figure = figures.create_countries_treemap(df, 'export', 'All years'))), width = 6)
            ]), body = True
            ), width = {'size':8, 'offset':2})
        ], style = {'padding-bottom':'2rem'}),
    
    
        html.P(["""A treemap is the ideal chart to display tree-structured data, which is the case of bilateral 
        trade data, since the Harmonized System is built around the idea of identifying and distributing products
        into certain groups of different levels, and since countries are also grouped into continents.""",
        """A treemap is a collection of rectangles with different colors and sizes, that are usually ordered by size
        from largest (top left) to smallest (bottom right). Hierarchy of categories in a treemap chart is represented as
        triangles inside other triangles (as countries fall under continents, and chapters fall under sections, etc.).
        The size and place of a rectangle defines how much money is traded between Lebanon and his partners for
        certain product categories."""],style = PARAGRAPH_STYLE),  
    
        html.Br(),
    
        dbc.Row(html.H4('Time Series', className = 'display-4', style = {'padding-left':'15px'})),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dcc.Graph(
                        figure = figures.create_time_series(df, 'import')
                    )
                    , body = True
                ),width = {'size':8, 'offset':2}
            ), style = {'padding-bottom':'2rem'}
        ),
        html.P(["""The chart above illustrates how Lebanon's total sum of trade value is moving over time. A user will play
        with the dropdown menus to filter the dataframe rendering the line chart. As well, he may click on a treemap 
        and hover over the other one for more detailed filtering and a very narrow view of trade vs time. For example, 
        a user may observe how much worth of gold is exported from Lebanon to Switzerland between 2011 and 2019 using
        Dash App 1, by first setting """, html.B('Select Depth Level'), ' and ', html.B('Select Trade Flow'), ' to ',
        html.I('2'), ' and ', html.I('Export'), """ respectively, then by clicking on 'Gold' rectangle in the first treemap
        and hovering over Switzerland's rectangle in the second treemap."""], style = PARAGRAPH_STYLE)
    ])


dash1 = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Label('Select HS Level', style = {'fontSize':'15px'}),
            dbc.Select(id = 'hs 1',
                       options = [{'label':'1','value':1},
                                  {'label':'2','value':2}],
                       value = 2,
                       size = 'lg')
        ],width = 2),
        
        dbc.Col([
            dbc.Label('Select Trade Flow', style = {'fontSize':'15px'}),
            dbc.Select(id = 'flow 1',
                       options = [{'label':'export','value':'export'},
                                  {'label':'import','value':'import'}],
                       value = 'export',
                       size = 'lg')
        ], width = 2),
        
        dbc.Col([
            dbc.Label('Select Year', style = {'fontSize':'15px'}),
            dbc.Select(id = 'year 1',
                       options = [{'label':'All years','value':'All years'},
                                  {'label':'2019', 'value':2019},
                                  {'label':'2018', 'value':2018},
                                  {'label':'2017', 'value':2017},
                                  {'label':'2016', 'value':2016},
                                  {'label':'2015', 'value':2015},
                                  {'label':'2014', 'value':2014},
                                  {'label':'2013', 'value':2013},
                                  {'label':'2012', 'value':2012},
                                  {'label':'2011', 'value':2011}],
                       value = 'All years',
                       size = 'lg')
        ], width = 2),
        
        dbc.Col([
            dbc.Label('Select Range of Years', style = {'fontSize':'15px'}),
            dcc.RangeSlider(id = 'slider 1', min = 2011, max = 2019, step = 1, value = [2014,2019], pushable = True,
                            marks = {year:{'label':str(year)} for year in range(2011,2020)}, disabled = True)
        ], width = 5),
        
        dbc.Col([
            dbc.Row(dbc.Button('Submit', id = 'submit 1', color = 'success', n_clicks = 0))
        ], width = 1, style = {'padding-right':'2rem'})
    ], style = {'padding-bottom':'1rem', 'padding-top':'1rem'}),
    
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'treemap 1_1'), type = 'circle'), body = True), width = 6),
        dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'treemap 1_2', clear_on_unhover = True), type = 'circle'),
                         body = True), width = 6)
    ], style = {'padding-bottom':'1rem'}),
    
    dbc.Row(dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'time series 1'), type = 'circle'), body = True), width = 12))
    
])


dash2 = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Label('Select HS Level', style = {'fontSize':'15px'}),
            dbc.Select(id = 'hs 2',
                       options = [{'label':'1','value':1},
                                  {'label':'2','value':2}],
                       value = 2,
                       size = 'lg')
        ],width = 2),
        
        dbc.Col([
            dbc.Label('Select Trade Flow', style = {'fontSize':'15px'}),
            dbc.Select(id = 'flow 2',
                       options = [{'label':'export','value':'export'},
                                  {'label':'import','value':'import'}],
                       value = 'export',
                       size = 'lg')
        ], width = 2),
        
        dbc.Col([
            dbc.Label('Select Year', style = {'fontSize':'15px'}),
            dbc.Select(id = 'year 2',
                       options = [{'label':'All years','value':'All years'},
                                  {'label':'2019', 'value':2019},
                                  {'label':'2018', 'value':2018},
                                  {'label':'2017', 'value':2017},
                                  {'label':'2016', 'value':2016},
                                  {'label':'2015', 'value':2015},
                                  {'label':'2014', 'value':2014},
                                  {'label':'2013', 'value':2013},
                                  {'label':'2012', 'value':2012},
                                  {'label':'2011', 'value':2011}],
                       value = 'All years',
                       size = 'lg')
        ], width = 2),
        
        dbc.Col([
            dbc.Label('Select Range of Years', style = {'fontSize':'15px'}),
            dcc.RangeSlider(id = 'slider 2', min = 2011, max = 2019, step = 1, value = [2014,2019], pushable = True,
                            marks = {year:{'label':str(year)} for year in range(2011,2020)}, disabled = True)
        ], width = 5),
        
        dbc.Col([
            dbc.Row(dbc.Button('Submit', id = 'submit 2', color = 'success', n_clicks = 0))
        ], width = 1, style = {'padding-right':'2rem'})
    ], style = {'padding-bottom':'1rem', 'padding-top':'1rem'}),
    
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'treemap 2_1'), type = 'circle'), body = True), width = 6),
        dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'treemap 2_2', clear_on_unhover = True), type = 'circle'),
                         body = True), width = 6)
    ], style = {'padding-bottom':'1rem'}),
    
    dbc.Row(dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'time series 2'), type = 'circle'), body = True), width = 12))
    
])


dash3 = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Label('Select HS Level', style = {'fontSize':'15px'}),
            dbc.Select(id = 'hs 3',
                       options = [{'label':'1','value':1},
                                  {'label':'2','value':2}],
                       value = 2,
                       size = 'lg')
        ],width = 2),
        
        dbc.Col([
            dbc.Label('Select Trade Flow', style = {'fontSize':'15px'}),
            dbc.Select(id = 'flow 3',
                       options = [{'label':'export','value':'export'},
                                  {'label':'import','value':'import'}],
                       value = 'export',
                       size = 'lg')
        ], width = 2),
        
        dbc.Col([
            dbc.Label('Select Year', style = {'fontSize':'15px'}),
            dbc.Select(id = 'year 3',
                       options = [{'label':'All years','value':'All years'},
                                  {'label':'2019', 'value':2019},
                                  {'label':'2018', 'value':2018},
                                  {'label':'2017', 'value':2017},
                                  {'label':'2016', 'value':2016},
                                  {'label':'2015', 'value':2015},
                                  {'label':'2014', 'value':2014},
                                  {'label':'2013', 'value':2013},
                                  {'label':'2012', 'value':2012},
                                  {'label':'2011', 'value':2011}],
                       value = 'All years',
                       size = 'lg', disabled = True)
        ], width = 2),
        
        dbc.Col([
            dbc.Label('Select Range of Years', style = {'fontSize':'15px'}),
            dcc.RangeSlider(id = 'slider 3', min = 2011, max = 2019, step = 1, value = [2014,2019], pushable = True,
                            marks = {year:{'label':str(year)} for year in range(2011,2020)})
        ], width = 5),
        
        dbc.Col([
            dbc.Row(dbc.Button('Submit', id = 'submit 3', color = 'success', n_clicks = 0))
        ], width = 1, style = {'padding-right':'2rem'})
    ], style = {'padding-bottom':'1rem', 'padding-top':'1rem'}),
    
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'treemap 3_1'), type = 'circle'), body = True), width = 6),
        dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'treemap 3_2', clear_on_unhover = True), type = 'circle' ),
                         body = True), width = 6)
    ], style = {'padding-bottom':'1rem'}),
    
    dbc.Row(dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'time series 3'), type = 'circle'), body = True), width = 12))
    
])


dash4 = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Label('Select HS Level', style = {'fontSize':'15px'}),
            dbc.Select(id = 'hs 4',
                       options = [{'label':'1','value':1},
                                  {'label':'2','value':2}],
                       value = 2,
                       size = 'lg')
        ],width = 2),
        
        dbc.Col([
            dbc.Label('Select Trade Flow', style = {'fontSize':'15px'}),
            dbc.Select(id = 'flow 4',
                       options = [{'label':'export','value':'export'},
                                  {'label':'import','value':'import'}],
                       value = 'export',
                       size = 'lg')
        ], width = 2),
        
        dbc.Col([
            dbc.Label('Select Year', style = {'fontSize':'15px'}),
            dbc.Select(id = 'year 4',
                       options = [{'label':'All years','value':'All years'},
                                  {'label':'2019', 'value':2019},
                                  {'label':'2018', 'value':2018},
                                  {'label':'2017', 'value':2017},
                                  {'label':'2016', 'value':2016},
                                  {'label':'2015', 'value':2015},
                                  {'label':'2014', 'value':2014},
                                  {'label':'2013', 'value':2013},
                                  {'label':'2012', 'value':2012},
                                  {'label':'2011', 'value':2011}],
                       value = 'All years',
                       size = 'lg', disabled = True)
        ], width = 2),
        
        dbc.Col([
            dbc.Label('Select Range of Years', style = {'fontSize':'15px'}),
            dcc.RangeSlider(id = 'slider 4', min = 2011, max = 2019, step = 1, value = [2014,2019], pushable = True,
                            marks = {year:{'label':str(year)} for year in range(2011,2020)})
        ], width = 5),
        
        dbc.Col([
            dbc.Row(dbc.Button('Submit', id = 'submit 4', color = 'success', n_clicks = 0))
        ], width = 1, style = {'padding-right':'2rem'})
    ], style = {'padding-bottom':'1rem', 'padding-top':'1rem'}),
    
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'treemap 4_1'), type = 'circle'), body = True), width = 6),
        dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'treemap 4_2', clear_on_unhover = True), type = 'circle'),
                         body = True), width = 6)
    ], style = {'padding-bottom':'1rem'}),
    
    dbc.Row(dbc.Col(dbc.Card(dcc.Loading(dcc.Graph(id = 'time series 4'), type = 'circle'), body = True), width = 12))
    
])


dash_page = html.Div([
    dbc.Row(html.H1('Dash App', className = 'display-1', style = {'padding-left':'15px'})),
    html.Hr(),
    dbc.Tabs([
        dbc.Tab(dash1, label = 'Dash App 1', label_style = {'fontSize':'15px'}),
        dbc.Tab(dash2, label = 'Dash App 2', label_style = {'fontSize':'15px'}),
        dbc.Tab(dash3, label = 'Dash App 3', label_style = {'fontSize':'15px'}),
        dbc.Tab(dash4, label = 'Dash App 4', label_style = {'fontSize':'15px'}),
    ])
])


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#183340"
}

# the styles for the main content position it to the right of the sidebar and add some padding.
CONTENT_STYLE = {
    "margin-left": "20rem",
    "padding": "2rem 1rem",
    "background-color":"#fcfcfc",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "right": 0,
#     "position": "fixed",
}

# the style for navigation links, to make it inline with the sidebar.
LINK_STYLE = {
    'border-radius':'5px',
    'fontSize':'15px',
    'color':'#3f5257',
    'background-color':'#fcfcfc'
}

sidebar = html.Div(
    [
        html.H2("Lebanon's Trade Performance", className="display-4", style = {'color':'#fafafa'}),
        html.Hr(style = {'border-top':'1px double #f7f7f7'}),
        dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink("Home", href="/page-1", id="page-1-link",
                                    active = True, style = LINK_STYLE)),
            dbc.NavItem(dbc.NavLink("Harmonized System", href="/page-2", id="page-2-link", 
                                    active = True, style = LINK_STYLE)),
            dbc.NavItem(dbc.NavLink("User Guide", href="/page-3", id="page-3-link",
                                    active = True, style = LINK_STYLE)),
            dbc.NavItem(dbc.NavLink("Dash App", href="/page-4", id="page-4-link",
                                    active = True, style = LINK_STYLE)),            
        ],
            vertical=True, pills = True, fill = True, style = {'padding-top':'2em'}
                ),
        
        dbc.Card(dbc.CardImg(src = '/assets/aub-osb.png'),
                 body = True, style = {'height':'95px', 'position':'absolute', 'bottom':15, 'right':5, 'left':5})
    
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)
