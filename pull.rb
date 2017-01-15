
#[num,content,pic_text,photo_comic_gif,standard_original,animal_people_not]


current_meme = [1,3,1,2,1,2]
new_meme = [0,0,0,0,0,0]
yes_no = 1
current_rand = [[1,1],[1,1,1,1],[1,1],[1,1,1],[1,1],[1,1,1]]

loop do

puts ("Current Meme:")
print current_meme
puts "\n"
# puts "Is the meme dank? (-1 or 1)\n"
# yes_no = gets.chomp.to_i

for i in 0..5 do
  if current_rand[i][current_meme[i]] <= 0.1*current_rand[i].inject(0, &:+)
   current_rand[i][current_meme[i]] += 2 * yes_no
 else
    current_rand[i][current_meme[i]] += 0.1 * yes_no
  end
   if current_rand[i][current_meme[i]] <= 1
     current_rand[i][current_meme[i]] = 1
   end
end


for i in 0..5 do
   for j in 0..current_rand[i].length-1 do
     if current_rand[i][j] > rand(0..current_rand[i].inject(0, &:+))
      new_meme[i] = j
     end
   end
 end

print "Dist."
print current_rand
print "\n"
print "New."
print new_meme
print "\n"

current_meme= new_meme
end
