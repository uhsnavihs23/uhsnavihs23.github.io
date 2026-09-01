from tailwind_redesign import get_header, get_footer, get_tailwind_head

html = get_tailwind_head("India Market Tracker", 2) + get_header(2, 'projects') + '''
    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 py-12 w-full">
        <div class="flex flex-col md:flex-row justify-between items-end mb-8 border-b border-gray-200 pb-6 gap-4">
            <div>
                <h1 class="text-4xl font-extrabold text-primary mb-2">India Market Tracker</h1>
                <p class="text-secondary text-lg">Real-time market dashboard powered by TradingView.</p>
            </div>
            <div>
                <div class="inline-flex items-center px-4 py-2 bg-emerald-50 border border-emerald-200 rounded-lg shadow-sm">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 mr-2 animate-pulse"></span>
                    <span class="text-sm font-bold text-emerald-700 uppercase tracking-wide">Live Markets</span>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
            <!-- Nifty 50 -->
            <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
                <div class="p-4 border-b border-gray-100 bg-gray-50 flex justify-between items-center">
                    <h2 class="text-lg font-bold text-primary">NIFTY 50</h2>
                    <span class="text-xs font-bold text-gray-500 bg-gray-200 px-2 py-1 rounded">NSE</span>
                </div>
                <div class="h-[400px] w-full">
                    <!-- TradingView Widget BEGIN -->
                    <div class="tradingview-widget-container" style="height:100%;width:100%">
                      <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
                      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
                      {
                      "autosize": true,
                      "symbol": "NSE:NIFTY",
                      "interval": "D",
                      "timezone": "Asia/Kolkata",
                      "theme": "light",
                      "style": "2",
                      "locale": "in",
                      "enable_publishing": false,
                      "backgroundColor": "rgba(255, 255, 255, 1)",
                      "gridColor": "rgba(240, 243, 250, 0)",
                      "hide_top_toolbar": true,
                      "hide_legend": true,
                      "save_image": false,
                      "container_id": "tradingview_nifty",
                      "support_host": "https://www.tradingview.com"
                    }
                      </script>
                    </div>
                    <!-- TradingView Widget END -->
                </div>
            </div>

            <!-- Sensex -->
            <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
                <div class="p-4 border-b border-gray-100 bg-gray-50 flex justify-between items-center">
                    <h2 class="text-lg font-bold text-primary">SENSEX</h2>
                    <span class="text-xs font-bold text-gray-500 bg-gray-200 px-2 py-1 rounded">BSE</span>
                </div>
                <div class="h-[400px] w-full">
                    <!-- TradingView Widget BEGIN -->
                    <div class="tradingview-widget-container" style="height:100%;width:100%">
                      <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
                      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
                      {
                      "autosize": true,
                      "symbol": "BSE:SENSEX",
                      "interval": "D",
                      "timezone": "Asia/Kolkata",
                      "theme": "light",
                      "style": "2",
                      "locale": "in",
                      "enable_publishing": false,
                      "backgroundColor": "rgba(255, 255, 255, 1)",
                      "gridColor": "rgba(240, 243, 250, 0)",
                      "hide_top_toolbar": true,
                      "hide_legend": true,
                      "save_image": false,
                      "container_id": "tradingview_sensex",
                      "support_host": "https://www.tradingview.com"
                    }
                      </script>
                    </div>
                    <!-- TradingView Widget END -->
                </div>
            </div>
        </div>

        <!-- Gold & USD/INR -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- Gold Spot -->
            <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
                <div class="p-4 border-b border-gray-100 bg-gray-50 flex justify-between items-center">
                    <h2 class="text-lg font-bold text-primary">GOLD SPOT (MCX)</h2>
                    <span class="text-xs font-bold text-gray-500 bg-gray-200 px-2 py-1 rounded">MCX</span>
                </div>
                <div class="h-[300px] w-full">
                    <!-- TradingView Widget BEGIN -->
                    <div class="tradingview-widget-container" style="height:100%;width:100%">
                      <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
                      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
                      {
                      "autosize": true,
                      "symbol": "MCX:GOLD1!",
                      "interval": "D",
                      "timezone": "Asia/Kolkata",
                      "theme": "light",
                      "style": "2",
                      "locale": "in",
                      "enable_publishing": false,
                      "backgroundColor": "rgba(255, 255, 255, 1)",
                      "gridColor": "rgba(240, 243, 250, 0)",
                      "hide_top_toolbar": true,
                      "hide_legend": true,
                      "save_image": false,
                      "container_id": "tradingview_gold",
                      "support_host": "https://www.tradingview.com"
                    }
                      </script>
                    </div>
                    <!-- TradingView Widget END -->
                </div>
            </div>
            
            <!-- USD/INR -->
            <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
                <div class="p-4 border-b border-gray-100 bg-gray-50 flex justify-between items-center">
                    <h2 class="text-lg font-bold text-primary">USD / INR</h2>
                    <span class="text-xs font-bold text-gray-500 bg-gray-200 px-2 py-1 rounded">FOREX</span>
                </div>
                <div class="h-[300px] w-full">
                    <!-- TradingView Widget BEGIN -->
                    <div class="tradingview-widget-container" style="height:100%;width:100%">
                      <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
                      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
                      {
                      "autosize": true,
                      "symbol": "FX_IDC:USDINR",
                      "interval": "D",
                      "timezone": "Asia/Kolkata",
                      "theme": "light",
                      "style": "2",
                      "locale": "in",
                      "enable_publishing": false,
                      "backgroundColor": "rgba(255, 255, 255, 1)",
                      "gridColor": "rgba(240, 243, 250, 0)",
                      "hide_top_toolbar": true,
                      "hide_legend": true,
                      "save_image": false,
                      "container_id": "tradingview_usdinr",
                      "support_host": "https://www.tradingview.com"
                    }
                      </script>
                    </div>
                    <!-- TradingView Widget END -->
                </div>
            </div>
        </div>

    </main>
''' + get_footer(2)

with open('./projects/market-tracker/index.html', 'w') as f:
    f.write(html)
