package hello.hellobigcon.security.filter;

import com.fasterxml.jackson.databind.ObjectMapper;
import hello.hellobigcon.common.jwt.JwtTokenProvider;
import hello.hellobigcon.common.jwt.errors.JwtLogoutException;
import io.jsonwebtoken.ExpiredJwtException;
import io.jsonwebtoken.JwtException;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@Component
@RequiredArgsConstructor
@Slf4j
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    private final JwtTokenProvider jwtTokenProvider;
    private final ObjectMapper objectMapper;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        try {
            String token = resolveToken(request);
            if (token != null && jwtTokenProvider.validateToken(token)) {
                // TODO 로그아웃 확인 기능 추가 필요

                String userEmail = jwtTokenProvider.getEmail(token);

                UserDetails userDetails = User.builder()
                        .username(userEmail)
                        .password("") // 패스워드 필요 없음
                        .roles("USER")
                        .build();

                Authentication authentication = new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
                SecurityContextHolder.getContext().setAuthentication(authentication);
            }

            filterChain.doFilter(request, response);
        } catch (JwtLogoutException e){
            log.warn("JWT Expired By Logout : message={}", e.getMessage());
            setErrorResponse(response, e.getMessage());
        } catch (ExpiredJwtException e){
            log.warn("JWT Expired : message={}", e.getMessage());
            setErrorResponse(response, "JWT 토큰이 만료되었습니다.");
        } catch (JwtException | IllegalArgumentException e){
            log.error("JWT Error : message={}", e.getMessage(), e);
            setErrorResponse(response, "JWT 토큰 확인에 실패했습니다.");
        }
    }

    private void setErrorResponse(HttpServletResponse response, String message) throws IOException {
        response.setStatus(HttpServletResponse.SC_UNAUTHORIZED); // 401 Unauthorized
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");

        // 에러 메시지 구성
        Map<String, String> errorResponse = new HashMap<>();
        errorResponse.put("success", "false");
        errorResponse.put("message", message);

        // JSON으로 응답 반환
        objectMapper.writeValue(response.getWriter(), errorResponse);
    }

    private String resolveToken(HttpServletRequest request) {
        String bearerToken = request.getHeader("Authorization");
        if (bearerToken != null && bearerToken.startsWith("Bearer ")) {
            return bearerToken.substring(7);
        }
        return null;
    }

}
