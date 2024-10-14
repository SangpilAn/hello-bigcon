# weather.py
import streamlit as st
import streamlit.components.v1 as components

def show_weather():
  components.html("""
                  <script>
                  (function(d, s, id) {
                    if (d.getElementById(id)) {
                      if (window.__TOMORROW__) {
                        window.__TOMORROW__.renderWidget();
                      }
                    return;
                    }
                  const fjs = d.getElementsByTagName(s)[0];
                  const js = d.createElement(s);
                  js.id = id;
                  js.src = "https://www.tomorrow.io/v1/widget/sdk/sdk.bundle.min.js";

                  fjs.parentNode.insertBefore(js, fjs);
                  })(document, 'script', 'tomorrow-sdk');
                  </script>

                  <div class="tomorrow"
                  data-location-id="065406"
                  data-language="KO"
                  data-unit-system="METRIC"
                  data-skin="light"
                  data-widget-type="upcoming"
                  style="padding-bottom:22px;position:relative;"
                  >
                  <a
                  href="https://www.tomorrow.io/weather-api/"
                  rel="nofollow noopener noreferrer"
                  target="_blank"
                  style="position: absolute; bottom: 0; transform: translateX(-50%); left: 50%;"
                  >
                  <img
                  alt="Powered by the Tomorrow.io Weather API"
                  src="https://weather-website-client.tomorrow.io/img/powered-by.svg"
                  width="250"
                  height="18"
                  />
                  </a>
                  </div>
                  """, height=900)