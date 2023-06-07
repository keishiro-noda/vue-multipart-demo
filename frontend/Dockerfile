FROM node:18-alpine

WORKDIR /home/guest/my-vue-app/frontend

COPY . .
RUN yarn install \
    && yarn build \
    && yarn global add @vue/cli @vue/cli-init \
    && npm install -g serve

CMD ["bash"]