<%@ page trimDirectiveWhitespaces="true" %> # đầu tiên là loại bỏ hoàn toàn các khoảng trắng
<%
String filepath = getServletContext().getRealPath("resources") + "/"; # lấy filepath ta có sử dụng getServletContext
String _file = request.getParameter("file");

response.setContentType("image/jpeg");
try{
    java.io.FileInputStream fileInputStream = new java.io.FileInputStream(filepath + _file);
    int i;   
    while ((i = fileInputStream.read()) != -1) {  
        out.write(i);
    }   
    fileInputStream.close();
}catch(Exception e){
    response.sendError(404, "Not Found !" );
}
%>