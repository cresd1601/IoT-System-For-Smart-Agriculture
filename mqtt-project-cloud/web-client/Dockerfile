# Stage 1: Dependencies
FROM node:18-alpine AS deps

WORKDIR /app

# Only copy package.json if package-lock.json does not exist
COPY package.json ./

RUN npm install --production

# Stage 2: Build
FROM node:18-alpine AS build

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .

RUN NEXT_PUBLIC_CLOUD_SERVICE_IP=APP_NEXT_PUBLIC_CLOUD_SERVICE_IP npm run build

# Stage 3: Production
FROM node:18-alpine AS production

WORKDIR /app

COPY --from=build /app /app

ENV NODE_ENV=production

RUN chmod +x /app/entrypoint.sh

EXPOSE 3000

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["npm", "start"]
