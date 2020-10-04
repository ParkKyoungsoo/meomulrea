<template>
	<v-row justify="center">
		<v-expansion-panels inset>
			<v-expansion-panel>
				<v-expansion-panel-header>답글 달기</v-expansion-panel-header>
				<v-expansion-panel-content>
					<v-textarea
						outlined
						name="input-7-4"
						label="답글을 남겨보세요." 
						:value="comment"
						
						color="orange"
					></v-textarea>
				
					<div class="text-right">
						<!-- <v-btn v-show="myComment == 0" @click="msgComment(myComment)" color="gray" style="color:darkgray">등록</v-btn> -->
						<v-btn @click="$emit('comment', comment)" color="orange">등록</v-btn>
					</div>
				</v-expansion-panel-content>
			</v-expansion-panel>
		</v-expansion-panels>
	</v-row>
</template>

<script>
export default {
	name: 'Comment',
	props: {
		comment: String,
	},
	// registerComment(idx) {
  //     console.log("idx" , idx)
  //     console.log("내 유저타입은?")
  //     console.log(this.myComment)
  //     axios.post(baseURL + `api/reviews/${idx}/create_reply/`, {
  //       content: this.myComment,
  //     },
  //     {
  //       headers: {
  //         Authorization: `Token ${this.$cookies.get("auth-token")}`,
  //       },
  //     })
  //     .then(res => {
  //       console.log("사장님 댓글", res.data)
  //     })
  //     .catch(err => 
  //     {
  //       console.log('답글ㄴㄴ', err.response)
  //     })
  //   },
}
</script>

<style>

</style>