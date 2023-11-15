FROM nginx:alpine

# Copy the entire 'html' directory to Nginx's serve directory
COPY html/ /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start Nginx when the container has provisioned
CMD ["nginx", "-g", "daemon off;"]