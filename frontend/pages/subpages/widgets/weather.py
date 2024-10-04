# weather.py
import streamlit as st
import streamlit.components.v1 as components

def show_weather():
  # 날씨 1
  components.html("""
                <div id="ww_9fca590b9f788" v='1.3' loc='id' a='{"t":"horizontal","lang":"ko","sl_lpl":1,"ids":["wl7477"],
                  "font":"Malgun Gothic","sl_ics":"one_a","sl_sot":"celsius","cl_bkg":"#FFFFFF","cl_font":"#000000",
                  "cl_cloud":"#d4d4d4","cl_persp":"#2196F3","cl_sun":"#FFC107","cl_moon":"#FFC107","cl_thund":"#FF5722"}'
                  style="border-radius: 15px; overflow: hidden;">
                  More forecasts:
                  <a href="https://oneweather.org/seoul/30_days/" id="ww_9fca590b9f788_u" target="_blank">Seoul 30 day forecast</a>
                </div>
                  <script async src="https://app3.weatherwidget.org/js/?id=ww_9fca590b9f788"></script>
                  """,
                  height=280)
  # 날씨 2
  components.html("""
                  <a class="weatherwidget-io" href="https://forecast7.com/en/33d49126d50/jeju-do/" data-label_1="제주" data-label_2="WEATHER"
                  data-font="Noto Sans" data-icons="Climacons Animated" data-theme="original" >제주 WEATHER</a>
                  <script>
                  !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;
                  js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
                  </script>
                  """, height=550)
  # 날씨 3
  components.html("""
                  <script>
                  (function(d, s, id) {
                  if (d.getElementById(id)) {
                    if (window.__TOMORROW__) {
                      window.__TOMORROW__.renderWidget();
                      } return;
                    }
                  const fjs = d.getElementsByTagName(s)[0];
                  const js = d.createElement(s);
                  js.id = id;
                  js.src = "https://www.tomorrow.io/v1/widget/sdk/sdk.bundle.min.js";
                  fjs.parentNode.insertBefore(js, fjs);
                  })(document, 'script', 'tomorrow-sdk');
                  </script>
                  <div class="tomorrow" data-location-id="" data-language="KO" data-unit-system="METRIC"
                  data-skin="light" data-widget-type="upcoming" style="padding-bottom:22px;position:relative;">
                  <a
                  href="https://www.tomorrow.io/weather-api/" rel="nofollow noopener noreferrer" target="_blank"
                  style="position: absolute; bottom: 0; transform: translateX(-50%); left: 50%;">
                    <img alt="Powered by the Tomorrow.io Weather API"
                    src="https://weather-website-client.tomorrow.io/img/powered-by.svg"
                    width="250" height="18"/>
                  </a>
                  </div>
                  """, height=900)